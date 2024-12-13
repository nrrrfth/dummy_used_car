# Database for Used Car Sales Website
SQL Relational Database implementation of Used Car Sales Website

# Backgroud Project
The project I worked on came from Pacmann's BI Engineer course. This project was created to learn how to build a database for a project 
application and understand the data retrieval process is one of the tasks of Software & Data Engineering.

In this project, I was given the task of building a relational database for a website that offers used car sales. 

An overview of this project is that anyone can offer their products (used cars) in the form of advertisements and
potential buyers can search by several categories.

# Designing the Database
- Mission Statement
- Create Table Structure
- Determine Table Relationship
- Business Rules
- Determine Views
- ER Diagram


## Mission Statement
Mission statement is an explanation of the purpose of the database and the problems it aims to solve

Database for Used Car Sales Website aims to:
- Manage the data of used car sellers and buyers by facilitating a secure and efficient online platform
- Manage the advertising feature for used cars
- Manage the bidding feature for buyers who are interested in a car by ensuring user data and product information can be managed properly

## Create Table Structure
- Create the required table and fields
- Determine the key
- Create a description of the function of each table
  
### All that is required:
- Sellers can sell used cars and advertise them on the website
- Sellers can advertise their used car more than once
- Buyers can buy used cars
- Buyers can make used car price offers to sellers through advertisement posted on the website

So, all that is required is seller, buyer, ads and also bid data

Here are the details of creating a table for Database Used Car Sales Website

| tabel Sellers | tabel Buyers |
| --- | --- |
| to store car seller information | to store car buyer information |
| seller_id: VARCHAR(255) NOT NULL PRIMARY KEY,  Auto Increment | buyer_id: VARCHAR(255) NOT NULL PRIMARY KEY, Auto Increment |
|name: VARCHAR(100), nama lengkap penjual |name: VARCHAR(100), nama lengkap pembeli
|email: VARCHAR(100), alamat email penjual (unique) |email: VARCHAR(100), alamat email pembeli (unique)
|password: VARCHAR(255), kata sandi penjual |password: VARCHAR(255), kata sandi pembeli
|contact_number: VARCHAR(20), nomor kontak penjual |contact_number: VARCHAR(20), nomor kontak pembeli
|location: VARCHAR(100), lokasi/domisili penjual |location: VARCHAR(100), lokasi/domisili pembeli
|registration_date: TIMESTAMP, waktu pendaftaran penjual |registration_date: TIMESTAMP, waktu pendaftaran pembeli
|status: ENUM(’Active’, ‘Inactive’), status akun penjual |status: ENUM(’Active’, ‘Inactive’), status akun pembeli
|rating: DECIMAL(10, 2), penilaian rata-rata dari pembeli |purchase_history: TEXT, catatan riwayat pembelian |
|number_of_sales: INTEGER, jumlah total penjualan yg telah diselesaikan| 

| tabel Ads | tabel Bids |
| --- | --- |
| to store ads information | to store bids information |
| ad_id: VARCHAR(255) NOT NULL PRIMARY KEY, Auto Increment | bid_id: VARCHAR(255) NOT NULL PRIMARY KEY Auto Increment |
| seller_id: VARCHAR(255), Foreign Key, referes to the Sellers table |  ad_id: VARCHAR(255), FOREIGN KEY, refers to the Ads table |
| title: VARCHAR(200), judul iklan | buyer_id: VARCHAR(255), Foreign Key, referes to the Buyers table |
| description: TEXT, deskripsi tambahan tentang mobil|  bid_amount: DECIMAL (12,2), jumlah penawaran yg diajukan oleh pembeli |
| car_brand: ENUM, merk mobil | location: VARCHAR(100), lokasi/domisili | status: ENUM(’Pending’, ‘Accepted’, ‘Rejected’), status penawaran |
| models:  VARCHAR(100), model mobil | bid_date: TIMESTAMP, waktu penawaran dilakukan |
| body_car_type: ENUM(’MPV’, ‘SUV’, ‘Van’, ‘Sedan’, ‘Hatcback’), type of car body | interaction_type: ENUM(’View’, ‘Bid’, Contract’), jenis interaksi |
| transmission: ENUM(’Manual’, ‘Automatic’) type of car transmission | bid_detail: TEXT, detail dari bid |
| year_of_manufacture: YEAR, year of car manufacture  |
| color: VARCHAR(30), color of car |
| mileage: INTEGER, jarak yang telah ditempuh dalam kilometer |
| engine: ENUM, machine spesification |
| price: DECIMAL(12,2), offered price |
| is_negotiable: BOOLEAN, apakah harga bisa dinegosiasi |
| created_at: TIMESTAMP, waktu iklan dibuat |
| updated_at: TIMESTAMP, waktu iklan terakhir diperbaharui |
| status: ENUM(’Active’, ‘Sold’, ‘Expired’), status iklan |
| image: TEXT, menyimpan url atau path ke gambar mobil |  

to be continued

### Determine Table Relationship





Now with docker!

# Installing dependencies
There are two condition;
## if you already build
1. If you use docker, just `docker-compose up -d --build` in order to re-build the container
## if you haven't
1. Just `docker-compose up -d` since this is the first time we are going to build the container

# How to docker
1. Make sure docker has been installed in your machine then,
2. go and `docker-compose up -d` and wait untill docker has build and run your container
3. go ahead and do `docker ps` and take a look what ID's is the container
4. execute this `docker exec -it [container_id] sh` and you will be greeted with container's sh
5. do `ls` to make sure there are .pys inside the container
6. all what you have to do just go and play around, have fun!

## How to access container sh
1. First of all, check container's id via `docker ps` and take a look `my-python-container` id is
2. then do this `docker exec -it [container_id] sh` to open sh inside container
3. check `ls` what inside, and then
4. have fun!
