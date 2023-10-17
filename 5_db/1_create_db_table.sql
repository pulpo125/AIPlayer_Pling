CREATE DATABASE finaldb CHARACTER SET utf8mb4 collate utf8mb4_general_ci;
create user 'django'@'%' identified by 'root1234';
grant all privileges on *.* to 'django'@'%' with grant option;
flush privileges;

use finaldb;
create table ply_meta(
	ply_id int not null primary key,
    ply_title varchar(500),
    ply_tag_lst TEXT,
    ply_like_cnt int,
    ply_updt varchar(100)
);

create table ply_title_embedding(
	emd_id int not null primary key auto_increment,
	ply_id int not null,
    ply_title_emd TEXT,
    FOREIGN KEY(ply_id) REFERENCES ply_meta(ply_id)
);

create table song_meta(
	song_id int not null primary key,
    song_name varchar(500),
    artist_name_lst text,
    song_gnr_lst text
);

create table song_in_ply(
	songinply_id int not null primary key auto_increment,
	ply_id int,
    song_id int,
    FOREIGN KEY(ply_id) REFERENCES ply_meta(ply_id),
    FOREIGN KEY(song_id) REFERENCES song_meta(song_id)
);

create table user_log(
	user_id int not null primary key auto_increment,
    user_title VARCHAR(500),
    user_title_embedding TEXT,
    user_song_id_lst TEXT,
    user_tag_lst TEXT,
    user_updt VARCHAR(100),
    user_like_cnt int
);
