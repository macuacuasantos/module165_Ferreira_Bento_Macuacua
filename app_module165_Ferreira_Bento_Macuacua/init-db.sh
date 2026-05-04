#!/bin/bash
mongoimport --db my_data_Ferreira_Bento_Macuacua --collection open_data --file /docker-entrypoint-initdb.d/open_data.json --jsonArray
mongoimport --db my_data_Ferreira_Bento_Macuacua --collection my_team --file /docker-entrypoint-initdb.d/my_team.json --jsonArray
