# ExaWorld
Exaworld, a project "per la simulazione di un ecosistema virtuale" (for a virtual ecosystem simulation) created by Bultrini Francesco, Ceccagnoli Andrea, Mariani Filippo, Mazza Giorgio for computer science's stage.

<h1 align=center>
<img src="landscape.png" width=100%>
</h1>

## Made up of 4 modules:
#### LOGIC
    logic map, hexagons and links generator
    
#### DATABASE
    database structure containing terrains, plants and animals. Made using psycopg2.

#### CONCEPT
    fills the map with procedurally generated tiles' values (temperature, humidity, altitude), terrains, plants and animals.

#### GRAPHIC
    3d models made in Blender and implementation via Panda3d engine
