-- filepath: c:\PostGress_Database\populate_bdd.sql

-- Insert products
-- Insert products avec origine
INSERT INTO Product (nom, description, ingredients, origine, prix) VALUES
('Crème Source Hydra', 'Soin hydratant intensif pour le visage', 'acide hyaluronique, aloé vera, camomille', 'France', 14.9),
('Crème Équilibre Jour', 'Crème légère pour usage quotidien', 'glycérine, vitamine E, extrait de thé vert', 'France', 13.5),
('Crème Nutrition Intense', 'Soin riche pour peau sèche ou déshydratée', 'beurre de karité, huile d’argan, céramides', 'Maroc', 15.8),
('Fluide Perfect Teint', 'Crème teintée effet naturel', 'pigments minéraux, acide hyaluronique, aloe vera', 'Corée du Sud', 16.5),
('Voile Éclat', 'Crème hydratante unifiante', 'niacinamide, mica, vitamine C', 'Japon', 17.2),
('Crème Lumière Teintée', 'Crème hydratante teintée avec fini lumineux', 'huile de jojoba, cacao, pigments végétaux', 'Italie', 17.9),
('Contour Regard Fraîcheur', 'Soin défatiguant pour le contour des yeux', 'caféine, acide hyaluronique, extrait de bleuet', 'Suisse', 12.9),
('Écran Solaire Quotidien SPF 50', 'Haute protection solaire sans résidu blanc', 'oxyde de zinc, aloe vera, vitamine E', 'Australie', 15.6),
('Crème Apaisante Douce Nuit', 'Soin réparateur après-soleil', 'menthol, aloe vera, calendula', 'Espagne', 11.8),
('Crème Cell Repair Nuit', 'Crème de nuit régénérante et nourrissante', 'rétinol, peptides, huile d’avocat', 'États-Unis', 19.9),
('Crème Riche Réconfort', 'Hydratation profonde pour peaux sensibles', 'huile d’amande douce, glycérine, panthénol', 'France', 13.8),
('Sérum Tenseur Immédiat', 'Lisse et raffermit le teint', 'collagène, acide hyaluronique, silice', 'Allemagne', 22.4),
('Gel Matifiant Jour', 'Contrôle la brillance et l’excès de sébum', 'extrait de bambou, zinc PCA, hamamélis', 'Corée du Sud', 12.2),
('Lotion Tonique Équilibrante', 'Resserre les pores et rafraîchit la peau', 'eau florale, extrait de concombre, allantoïne', 'France', 9.9),
('Crème Détox Antipollution', 'Protège la peau contre les agressions urbaines', 'charbon actif, thé vert, acide lactique', 'Canada', 18.1);


-- Insert promotions

-- Insert teinte peau et produits
INSERT INTO Teinte_Peau_Produits (teinte, id_product) VALUES
('claire', 1),
('claire', 4),
('claire', 8),
('moyenne claire', 2),
('moyenne claire', 5),
('moyenne claire', 8),
('moyenne', 2),
('moyenne', 5),
('moyenne', 10),
('moyenne foncée', 3),
('moyenne foncée', 6),
('moyenne foncée', 10),
('foncée', 3),
('foncée', 6),
('foncée', 9),
('très foncée', 3),
('très foncée', 6),
('très foncée', 9);