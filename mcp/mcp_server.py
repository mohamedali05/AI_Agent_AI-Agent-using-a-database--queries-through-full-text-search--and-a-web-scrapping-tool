import logging
import os
from typing import Dict, Any
from dataclasses import dataclass
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator
import psycopg2
from psycopg2.extensions import connection
from difflib import get_close_matches





import httpx
from mcp.server.fastmcp import FastMCP, Context
import time

time.sleep(5)
host = os.getenv("DB_HOST", "localhost")



# Connexion à la base de données PostgreSQL

MCP_PORT = int(os.getenv("MCP_PORT", "5001"))
DB_PORT = 5432
(print(f"Connecting to PostgreSQL at {host}:{DB_PORT}..."))


teintes_connues = ["claire", "moyenne", "foncée" , "moyenne claire" , 
                   "moyenne foncée" , "moyenne" , "foncée" , "très foncée"]


# Configuration du logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@dataclass
class AppContext:
    """Contexte de l'application MCP"""
    conn: connection

@asynccontextmanager
async def app_lifespan(_: FastMCP) -> AsyncIterator[AppContext]:
    """Initialise et nettoie les ressources au démarrage/arrêt."""
    logger.info("Connecting to PostgreSQL using psycopg2...")
    conn = psycopg2.connect(
    dbname="postgres",  
    user="postgres",
    password="3Gy5uwht4*",
    host=host,  
    port= DB_PORT,
    )
    yield AppContext(conn=conn)
    conn.close()
    logger.info("Connection to PostgreSQL closed.")


# Création du serveur MCP simple
mcp = FastMCP(
    "MCP Produits Beauté",
    description="Expose un outil de récupération de données via une requête SQL.",
    version="0.1.0",
    lifespan=app_lifespan,
    port=MCP_PORT,
    host="0.0.0.0", 
)


@mcp.tool()
def search_products(phrase: str, ctx: Context = None) -> Dict[str, Any]:
    """
    Recherche les produits en utilisant la similarité sur la concaténation de
    nom, description, ingrédients et origine.

    Paramètres :
    ----------
    phrase : str
        phrase de recherche pour trouver des produits pertinents.
    ctx : Context, optionnel
        Contexte d'exécution du serveur MCP contenant la connexion PostgreSQL.

    Retour :
    -------
    dict
        Un dictionnaire contenant :
        - "result" : liste des produits pertinents (nom, description, ingrédients, origine, prix)
        - "count" : nombre de produits trouvés
        - "error" : message d'erreur si la requête échoue
    """
    try:
        with ctx.request_context.lifespan_context.conn.cursor() as cur:
            cur.execute("""
                SELECT nom, description, ingredients, origine, prix,
                       similarity(
                           nom || ' ' || description || ' ' || ingredients || ' ' || origine, 
                           %s::text
                       ) AS score
                FROM Product
                WHERE similarity(
                          nom || ' ' || description || ' ' || ingredients || ' ' || origine, 
                          %s::text
                      ) > 0.1
                ORDER BY score DESC
                LIMIT 20;
            """, (phrase, phrase))
            
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            result = [dict(zip(columns, row)) for row in rows]
            return {"result": result, "count": len(result)}
    except Exception as e:
        logger.error(f"Similarity product search error: {e}")
        return {"error": str(e), "result": [], "count": 0}

    
@mcp.tool()
def recommended_products_by_skin_tone(teinte: str, ctx: Context = None) -> Dict[str, Any]:
    """
    Recommande des produits à partir de la teinte de peau, 
    en utilisant le full text search sur la table Teinte_Peau_Produits.

    Paramètres :
    ----------
    teinte : str
        la teinte de peau (ex. : "claire", "très foncée", "moyenne foncée").

    ctx : Context, optionnel
        Contexte d'exécution du serveur MCP contenant la connexion PostgreSQL.

    Retour :
    -------
    dict
        Un dictionnaire contenant :
        - "result" : liste des produits pertinents (nom, description, ingrédients, origine, prix)
        - "count" : nombre de produits trouvés
        - "error" : message d'erreur si la requête échoue
    """
    try:
        with ctx.request_context.lifespan_context.conn.cursor() as cur:
            cur.execute("""
                SELECT p.nom, p.description, p.ingredients, p.origine, p.prix
                FROM Product p
                JOIN Teinte_Peau_Produits t ON p.id = t.id_product
                WHERE to_tsvector('french', t.teinte) @@ plainto_tsquery('french', %s)
            """, (teinte,))
            rows = cur.fetchall()
            columns = [desc[0] for desc in cur.description]
            result = [dict(zip(columns, row)) for row in rows]
            return {"result": result, "count": len(result)}
    except Exception as e:
        logger.error(f"Skin tone search error: {e}")
        return {"error": str(e), "result": [], "count": 0}
    



def run_server(transport: str = "sse") -> None:
    """Point d'entrée pour exécuter le serveur MCP."""
    try:
        mcp.run(transport=transport)
    except KeyboardInterrupt:
        logger.info("Arrêt manuel du serveur MCP")
    except Exception as e:
        logger.error(f"Erreur au démarrage du serveur: {str(e)}")

if __name__ == "__main__":
    run_server()