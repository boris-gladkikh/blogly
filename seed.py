DROP DATABASE IF EXISTS blogly_user_test_case;
​
CREATE DATABASE blogly_user_test_case;
​
CREATE TABLE users (id SERIAL PRIMARY KEY, first_name TEXT, last_name TEXT, image_url TEXT);
​
​
INSERT INTO users (first_name, last_name, image_url) VALUES ('Bob', 'Hope', 'https://vignette.wikia.nocookie.net/ideas/images/0/00/It%27s_Fat_Albert.png/revision/latest/scale-to-width-down/340?cb=20170522213112');
INSERT INTO users (first_name, last_name, image_url) VALUES ('Jane', 'Smith', 'https://vignette.wikia.nocookie.net/ideas/images/0/00/It%27s_Fat_Albert.png/revision/latest/scale-to-width-down/340?cb=20170522213112');
INSERT INTO users (first_name, last_name, image_url) VALUES ('Melody', 'Jones', 'https://upload.wikimedia.org/wikipedia/en/b/b1/Unicron-idw.jpg');
INSERT INTO users (first_name, last_name, image_url) VALUES ('Sarah', 'Palmer', 'https://img1.looper.com/img/gallery/things-only-adults-notice-in-jem/intro-1569611978.jpg');
INSERT INTO users (first_name, last_name, image_url) VALUES ('Alex', 'Miller');
INSERT INTO users (first_name, last_name, image_url) VALUES ('Shana', 'Smith', 'https://upload.wikimedia.org/wikipedia/en/b/b1/Unicron-idw.jpg');
INSERT INTO users (first_name, last_name, image_url) VALUES ('Maya', 'Malarkin', 'https://img1.looper.com/img/gallery/things-only-adults-notice-in-jem/intro-1569611978.jpg');
Collapse



