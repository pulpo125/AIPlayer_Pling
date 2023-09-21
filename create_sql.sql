CREATE DATABASE finaldb CHARACTER SET utf8mb4 collate utf8mb4_general_ci;
create user django identified by 'root1234';
grant all privileges on finaldb.*To django;
flush privileges;

-- drop database finald; 

use finaldb;
create table ply_meta(
	ply_id int not null primary key,
    ply_title varchar(500),
    ply_tag_lst TEXT,
    ply_like_cnt int,
    ply_updt varchar(100)
);

create table ply_title_embedding(
	ply_title_embedding_id int not null primary key auto_increment,
	ply_id int not null,
    ply_title_emd TEXT,
    FOREIGN KEY(ply_id) REFERENCES ply_meta(ply_id)
);

create table ply_img(
	ply_img_id int not null primary key auto_increment,
	ply_id int not null,
    ply_img blob,
    FOREIGN KEY(ply_id) REFERENCES ply_meta(ply_id)
);

create table song_meta(
	song_id int not null primary key,
    song_name varchar(500),
    artist_name_lst text,
    song_gnr_lst text
);

create table song_in_ply(
	ply_id int not null,
    song_id int not null,
    CONSTRAINT song_in_ply_id PRIMARY KEY(ply_id, song_id),
    FOREIGN KEY(song_id) REFERENCES song_meta(song_id)
);
