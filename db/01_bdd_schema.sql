-- filepath: c:\PostGress_Database\bdd_schema.sql
-- Create database (optional if you already created it)

-- Connect to the database (psql will not execute this inside the file, see note below)
-- \c bbd

-- You can omit the CREATE DATABASE line if you’ll connect first, then run the rest.

-- Table: Product
CREATE TABLE Product (
    id SERIAL PRIMARY KEY,
    nom TEXT NOT NULL,
    description TEXT,
    ingredients TEXT,
    origine TEXT , 
    prix NUMERIC(10, 2) NOT NULL
);


-- Table: Teinte_Peau_Produits
CREATE TABLE Teinte_Peau_Produits (
    teinte TEXT NOT NULL, -- ex: claire, moyenne claire, très foncée
    id_product INTEGER REFERENCES Product(id) ON DELETE CASCADE,
    PRIMARY KEY (teinte, id_product)
);

ALTER TABLE Product
ADD COLUMN tsv tsvector GENERATED ALWAYS AS (
  to_tsvector('french', coalesce(nom, '') || ' ' || coalesce(description, '') || ' ' || coalesce(ingredients, '') || ' ' || coalesce(origine, '') || ' ' || prix::TEXT)
) STORED;

CREATE INDEX idx_product_tsv ON Product USING GIN(tsv);
CREATE EXTENSION IF NOT EXISTS pg_trgm;
