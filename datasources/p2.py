CREATE DATABASE project;
USE project

-- create table statements
CREATE TABLE IF NOT EXISTS genre (
   genreID INT PRIMARY KEY NOT NULL,
   genre VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS mediaType (
   mediaTypeID int PRIMARY KEY,
   type varchar(50)
);

CREATE TABLE IF NOT EXISTS media (
   mediaID int PRIMARY KEY,
   title varchar(100) NOT NULL,
   mediaType int NOT NULL,
   media int NOT NULL,
   rating int NOT NULL,
   genre int NOT NULL,
   mood int,
   FOREIGN KEY (genre)
        REFERENCES genre(genreID),
   FOREIGN KEY (mediaType)
        REFERENCES mediaType(mediaTypeID)
);

CREATE TABLE IF NOT EXISTS book (
   bookID int,
   author varchar(100) NOT NULL ,
   description varchar(2000),
   pages int NOT NULL,
   mediaID int NOT NULL,
   PRIMARY KEY (mediaID, bookID),
   FOREIGN KEY (mediaID)
         REFERENCES media(mediaID)
);


CREATE TABLE IF NOT EXISTS song (
   songID int,
   artist varchar(100) NOT NULL,
   BPM int NOT NULL,
   length int NOT NULL,
   mediaID int,
   PRIMARY KEY (mediaID, songID),
   FOREIGN KEY (mediaID)
         REFERENCES media(mediaID)
);


CREATE TABLE IF NOT EXISTS movie (
   movieID int,
   director varchar(100) NOT NULL,
   description varchar(2000),
   length int NOT NULL,
   mediaID int,
   PRIMARY KEY (mediaID, movieID),
   FOREIGN KEY (mediaID)
         REFERENCES media(mediaID)
);


CREATE TABLE IF NOT EXISTS colorScheme (
   colorSchemeID INT PRIMARY KEY NOT NULL,
   name VARCHAR(50) NOT NULL,
   headerColor VARCHAR(20) NOT NULL,
   textColor VARCHAR(20) NOT NULL,
   backgroundColor VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS mood (
   moodID INT PRIMARY KEY NOT NULL,
   name VARCHAR(50) NOT NULL,
   colorScheme INT NOT NULL,
   FOREIGN KEY (colorScheme)
       REFERENCES colorScheme(colorSchemeID)
);

CREATE TABLE IF NOT EXISTS user (
   userID INT PRIMARY KEY NOT NULL,
   name VARCHAR(100) NOT NULL,
   biography TEXT,
   email VARCHAR(100) NOT NULL,
   phoneNumber VARCHAR(20),
   mood INT NOT NULL,
   FOREIGN KEY (mood) REFERENCES mood(moodID)
);

CREATE TABLE IF NOT EXISTS review (
   reviewID int PRIMARY KEY,
   media int,
   description varchar(2000),
   rating int,
   user int,
   FOREIGN KEY (media)
       REFERENCES media(mediaID),
   FOREIGN KEY (user)
       REFERENCES user(userID)
);

CREATE TABLE IF NOT EXISTS log (
   userID INT NOT NULL,
   mediaID INT NOT NULL,
   favorite boolean,
   rating int,
   review VARCHAR(2000),
   logID int PRIMARY KEY,
   FOREIGN KEY (userID) REFERENCES user(userID),
   FOREIGN KEY (mediaID) REFERENCES media(mediaID)
);

CREATE TABLE IF NOT EXISTS journalEntry (
   journalID INT PRIMARY KEY NOT NULL,
   title VARCHAR(500) NOT NULL,
   text TEXT,
   user INT NOT NULL,
   date DATETIME,
   FOREIGN KEY (user)
       REFERENCES user(userID)
);

CREATE TABLE IF NOT EXISTS userGoal (
   goalID INT PRIMARY KEY NOT NULL,
   text TEXT,
   user INT NOT NULL,
   deadline DATE,
   FOREIGN KEY (user) REFERENCES user(userID)
);

-- insert statements
INSERT INTO colorScheme (ColorSchemeID, Name, HeaderColor, TextColor, BackgroundColor) VALUES
(1, 'Bright Day', '#FFFFFF', '#000000', '#FFFF00'),
(2, 'Deep Space', '#000033', '#FFFFFF', '#000066');


INSERT INTO mood (moodID, Name, colorScheme) VALUES
(1, 'Inspired', 1),
(2, 'Relaxed', 2),
(3, 'Sad', 2);


INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES
(1, 'Jack Dell', 'CEO of a tech startup, passionate about entrepreneurship and productivity.', 'jack.dell@aol.com', '787-555-0101', 1),
(2, 'Taylor Mack', 'Freelance writer with a keen interest in mindfulness and creative expression.', 'taylor.mack@gmail.com', '211-555-0102', 3),
(3, 'Ashton Bray', 'University student who loves culture and travel!', 'ashtonbrayyy@gmail.com', '443-187-8854', 1),
(4, 'Jason Bol', 'I love data!', 'jasonbol@yahoo.com', '301-444-1997', 2);


INSERT INTO mediaType (mediaTypeID, type) VALUES
(1, 'Song'),
(2, 'Book'),
(3, 'Movie');


INSERT INTO genre (genreID, genre) VALUES
(1, 'Business'),
(2, 'Self-Help'),
(3, 'Science Fiction'),
(4, 'Comedy'),
(5, 'Drama'),
(6, 'Pop');


INSERT INTO media (MediaID, title, mediaType, media, rating, genre, mood) VALUES
(1, 'Interstellar', 3, 1, 4.8, 5, 1),
(2, 'The Shawshank Redemption', 3, 2, 4.9, 5, 3),
(3, 'A Brief History of Time', 2, 1, 4.6, 3, 1),
(4, 'How to Win Friends & Influence People', 2, 2, 3.4, 2, 1),
(5, 'Shape of You', 1, 1, 4.5, 6, 2),
(6, 'Halo', 1, 2, 4.7, 6, 1);


INSERT INTO book (MediaID, BookID, Author, Description, Pages) VALUES
(3, 1, 'Stephen Hawking', 'A popular science book on cosmology.', 256),
(4, 2, 'Dale Carnegie', 'A self-help book about being the best.', 288);


INSERT INTO song (MediaID, SongID, Artist, BPM, Length) VALUES
(5, 1, 'Ed Sheeran', 95, 90),
(6, 2, 'Beyoncé', 120, 95);


INSERT INTO movie (MediaID, MovieID, Director, Description, Length) VALUES
(1, 1, 'Christopher Nolan', 'A team of explorers travel through a wormhole in space in an attempt to ensure humanitys survival.', 169),
(2, 2, 'Frank Darabont', 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.', 142);


INSERT INTO log (UserID, MediaID, Favorite, Rating, Review, logID) VALUES
(1, 1, true, 5, 'A cinematic masterpiece that goes beyond typical sci-fi. Thought-provoking and visually stunning.', 1),
(2, 5, true, 4.3, 'This song is so catchy! I cant stop listening to it. Ed Sheeran never disappoints.', 2),
(3, 3, false, 2.5, NULL, 3);


INSERT INTO journalEntry (JournalID, Title, Text, User, date) VALUES
(1, 'Daily Reflections', 'Felt inspired after watching Interstellar. Makes you think about our place in the universe. I want to watch some similar movies soon', 4, '2023-04-01'),
(2, 'Exploring Comedies', 'I really want to watch some more comedies. Recently I have seen a few Adam Sandler films and they really brought up my mood after a bad day!', 2, '2024-02-12');


INSERT INTO userGoal (GoalID, Text, User, Deadline) VALUES
(1, 'Read 12 business books this year', 4, '2023-12-31'),
(2, 'Practice mindfulness daily', 2, '2023-12-31');


/*Data for the table `mood` */
-- Generating color schemes
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (1, 'Olive', '#523a37', '#9588f3', '#e68750');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (2, 'MediumVioletRed', '#21e985', '#e99e10', '#9fb180');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (3, 'SkyBlue', '#60cd2a', '#998270', '#7c63d9');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (4, 'OldLace', '#bffe4e', '#a6a612', '#8f5355');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (5, 'FireBrick', '#9bfafa', '#37b2cf', '#ea12cc');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (6, 'Yellow', '#b0015b', '#b9a2f9', '#a9a647');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (7, 'Teal', '#91624c', '#241f5b', '#ac89c9');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (8, 'Orange', '#7cd811', '#caf7a9', '#8c7317');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (9, 'LightSeaGreen', '#eb0d7a', '#fad635', '#ed94ff');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (10, 'MediumSeaGreen', '#265404', '#9ec082', '#89588d');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (11, 'Teal', '#be1a85', '#397ef2', '#2486ef');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (12, 'BlanchedAlmond', '#bd9665', '#656906', '#5afd0b');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (13, 'YellowGreen', '#585968', '#21b081', '#6e6fd6');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (14, 'Brown', '#29c490', '#050eb2', '#9e75e9');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (15, 'Indigo', '#cc4812', '#776b11', '#32bc14');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (16, 'Pink', '#fa2e33', '#8cd6c9', '#bae692');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (17, 'Red', '#6dbc29', '#1ce14e', '#e2ed55');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (18, 'CornflowerBlue', '#ae2d6c', '#43354c', '#824327');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (19, 'SteelBlue', '#cde2cd', '#448857', '#f27e5b');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (20, 'SkyBlue', '#a99423', '#687e54', '#98bd8b');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (21, 'HotPink', '#28bec1', '#c137f6', '#e48602');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (22, 'GreenYellow', '#0f8072', '#e82d6e', '#a93512');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (23, 'DarkSalmon', '#780246', '#55594e', '#d146a9');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (24, 'White', '#1c33e3', '#e3068a', '#88e040');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (25, 'MediumPurple', '#d2245c', '#f6210f', '#aaf4ad');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (26, 'WhiteSmoke', '#668728', '#8fa789', '#f945bd');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (27, 'MediumSpringGreen', '#45b71e', '#42ede6', '#2759de');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (28, 'AntiqueWhite', '#aaad70', '#d47508', '#d449fd');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (29, 'LightBlue', '#72db03', '#85d4af', '#283771');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (30, 'Cornsilk', '#778315', '#4ddb19', '#199eaa');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (31, 'LightCoral', '#fa1cc4', '#09fbef', '#245392');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (32, 'White', '#e3db4a', '#42709b', '#b8ac8f');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (33, 'LightSalmon', '#6212ca', '#905d96', '#4dcbfb');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (34, 'MediumOrchid', '#2b0da2', '#d2b2f9', '#e248b3');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (35, 'Maroon', '#32ef1c', '#90b66a', '#d7e458');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (36, 'MediumSpringGreen', '#8ad696', '#17f9e3', '#40585a');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (37, 'LightCyan', '#bfc347', '#13fc6a', '#ce71f1');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (38, 'MidnightBlue', '#b46db5', '#72a3ce', '#6f4a90');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (39, 'DarkSlateGray', '#395e1d', '#8e3d2c', '#d9f103');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (40, 'CadetBlue', '#28544c', '#44a9f8', '#4f66bd');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (41, 'SteelBlue', '#c5a237', '#1547f7', '#ea190b');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (42, 'RosyBrown', '#9de518', '#b7718b', '#ad6197');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (43, 'Plum', '#e696d4', '#5464aa', '#fa4861');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (44, 'DarkSeaGreen', '#78dbd7', '#dee8a0', '#e5fd5e');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (45, 'DeepPink', '#8ac490', '#7ef293', '#3f3941');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (46, 'Orchid', '#8d092e', '#8bf154', '#f7c5c9');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (47, 'OliveDrab', '#dbaed9', '#1765d6', '#08c5a2');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (48, 'OliveDrab', '#69455c', '#39c402', '#dce7f2');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (49, 'DarkSalmon', '#b8df13', '#928dfa', '#151b95');
INSERT INTO colorScheme (colorSchemeID, name, headerColor, textColor, backgroundColor) VALUES (50, 'DarkMagenta', '#1c98fd', '#c41296', '#080f66');

-- Generating moods
INSERT INTO mood (moodID, name, colorScheme) VALUES (1, 'career', 48);
INSERT INTO mood (moodID, name, colorScheme) VALUES (2, 'site', 5);
INSERT INTO mood (moodID, name, colorScheme) VALUES (3, 'various', 27);
INSERT INTO mood (moodID, name, colorScheme) VALUES (4, 'international', 19);
INSERT INTO mood (moodID, name, colorScheme) VALUES (5, 'argue', 20);
INSERT INTO mood (moodID, name, colorScheme) VALUES (6, 'break', 8);
INSERT INTO mood (moodID, name, colorScheme) VALUES (7, 'culture', 31);
INSERT INTO mood (moodID, name, colorScheme) VALUES (8, 'product', 34);
INSERT INTO mood (moodID, name, colorScheme) VALUES (9, 'open', 33);
INSERT INTO mood (moodID, name, colorScheme) VALUES (10, 'alone', 48);
INSERT INTO mood (moodID, name, colorScheme) VALUES (11, 'test', 48);
INSERT INTO mood (moodID, name, colorScheme) VALUES (12, 'bed', 4);
INSERT INTO mood (moodID, name, colorScheme) VALUES (13, 'movie', 48);
INSERT INTO mood (moodID, name, colorScheme) VALUES (14, 'life', 50);
INSERT INTO mood (moodID, name, colorScheme) VALUES (15, 'buy', 12);
INSERT INTO mood (moodID, name, colorScheme) VALUES (16, 'off', 19);
INSERT INTO mood (moodID, name, colorScheme) VALUES (17, 'television', 22);
INSERT INTO mood (moodID, name, colorScheme) VALUES (18, 'beat', 42);
INSERT INTO mood (moodID, name, colorScheme) VALUES (19, 'oil', 39);
INSERT INTO mood (moodID, name, colorScheme) VALUES (20, 'soon', 33);
INSERT INTO mood (moodID, name, colorScheme) VALUES (21, 'office', 49);
INSERT INTO mood (moodID, name, colorScheme) VALUES (22, 'course', 39);
INSERT INTO mood (moodID, name, colorScheme) VALUES (23, 'community', 41);
INSERT INTO mood (moodID, name, colorScheme) VALUES (24, 'per', 46);
INSERT INTO mood (moodID, name, colorScheme) VALUES (25, 'bed', 18);
INSERT INTO mood (moodID, name, colorScheme) VALUES (26, 'growth', 3);
INSERT INTO mood (moodID, name, colorScheme) VALUES (27, 'writer', 40);
INSERT INTO mood (moodID, name, colorScheme) VALUES (28, 'tree', 32);
INSERT INTO mood (moodID, name, colorScheme) VALUES (29, 'until', 37);
INSERT INTO mood (moodID, name, colorScheme) VALUES (30, 'court', 40);
INSERT INTO mood (moodID, name, colorScheme) VALUES (31, 'before', 16);
INSERT INTO mood (moodID, name, colorScheme) VALUES (32, 'happy', 31);
INSERT INTO mood (moodID, name, colorScheme) VALUES (33, 'talk', 30);
INSERT INTO mood (moodID, name, colorScheme) VALUES (34, 'democratic', 15);
INSERT INTO mood (moodID, name, colorScheme) VALUES (35, 'case', 23);
INSERT INTO mood (moodID, name, colorScheme) VALUES (36, 'throughout', 22);
INSERT INTO mood (moodID, name, colorScheme) VALUES (37, 'your', 16);
INSERT INTO mood (moodID, name, colorScheme) VALUES (38, 'available', 39);
INSERT INTO mood (moodID, name, colorScheme) VALUES (39, 'box', 36);
INSERT INTO mood (moodID, name, colorScheme) VALUES (40, 'case', 40);
INSERT INTO mood (moodID, name, colorScheme) VALUES (41, 'player', 19);
INSERT INTO mood (moodID, name, colorScheme) VALUES (42, 'Congress', 44);
INSERT INTO mood (moodID, name, colorScheme) VALUES (43, 'type', 12);
INSERT INTO mood (moodID, name, colorScheme) VALUES (44, 'impact', 49);
INSERT INTO mood (moodID, name, colorScheme) VALUES (45, 'on', 1);
INSERT INTO mood (moodID, name, colorScheme) VALUES (46, 'theory', 18);
INSERT INTO mood (moodID, name, colorScheme) VALUES (47, 'thank', 37);
INSERT INTO mood (moodID, name, colorScheme) VALUES (48, 'north', 24);
INSERT INTO mood (moodID, name, colorScheme) VALUES (49, 'early', 31);
INSERT INTO mood (moodID, name, colorScheme) VALUES (50, 'authority', 42);

-- Generating users
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (1, 'Rebecca Farley', 'Above participant different performance car. Training look perform box. Appear free assume trouble away.
South ok significant prove statement. Right police specific everybody.', 'dylanhowell@example.com', '+1-906-721-4792x96068', 19);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (2, 'Shelly Reed', 'Memory should teach full. City page growth listen live miss.
Close name threat listen compare. Company couple cost Mr.
Else policy sea. Add support skill clear. Last during guess something.', 'john10@example.com', '327.639.5543x478', 34);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (3, 'Teresa Parker', 'Fall budget space institution letter office born. Century wear newspaper ask. Sign opportunity institution pick rate reason difference cost. Hotel author effect drop yard away class.', 'rebecca91@example.net', '(422)226-3989', 27);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (4, 'Christopher Banks', 'Want have letter seat. Trade area cultural boy participant. Yourself cultural manage first quite under.
Score large suggest brother watch forward show. Of very at nation.', 'jonesdebbie@example.org', '+1-782-797-3893x331', 53);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (5, 'Micheal Parks', 'Brother join represent strong. Audience environment animal education century.
Difficult cost meet. Civil cost line fund particular power office.', 'douglascummings@example.net', '(509)278-9749x15890', 25);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (6, 'Christine Calhoun', 'Report expect foreign democratic. Way there memory prevent new. Impact tax second now local.', 'sandovalsteven@example.com', '001-685-819-9963x6084', 6);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (7, 'Mitchell Jimenez', 'Traditional ever public low far stuff employee. Watch employee authority threat debate.
Above cold win class discover short. Research yard dream a doctor ability the around.', 'vle@example.org', '001-381-588-7385', 18);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (8, 'Timothy Parks', 'Authority cut we. Respond fund myself suddenly. These low region detail phone kind understand woman. Coach get red around more.', 'toddcooper@example.com', '+1-734-795-8548x98172', 9);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (9, 'Deborah Calhoun', 'Sell believe consider avoid dinner effort. Hot so partner put road together.
Many second concern blue. Building focus shake. Occur stuff mother open none case stay also.', 'crosbyjesse@example.net', '+1-238-977-4015x6687', 30);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (10, 'Melissa Morris', 'Three would pay away red might. Force purpose concern skin two fast fear.
Nor accept already training different. Phone evening develop industry image.', 'toddgibson@example.org', '692-851-1133', 36);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (11, 'Jonathan King', 'Leave region report begin business sort civil. Attention long be brother reduce avoid machine avoid. Field many thus.
Shoulder now mother cell pressure during.', 'pmartinez@example.org', '2118080948', 28);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (12, 'James Stafford', 'President education economy plan their us. Check city fine add kid significant action reveal.
While nothing field interview although kid short. Sing say watch ago.', 'jonesjulie@example.org', '(262)263-6549x2330', 55);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (13, 'Bethany Parker', 'Clearly themselves draw five. Direction fear shoulder tree this me. Decision how this city player usually.
Drop small see personal spring. Finally even step father.', 'garciajoseph@example.net', '+1-256-943-1291x484', 48);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (14, 'Mark Bennett', 'Nearly over voice senior. Economy happen maintain tend door.
Culture north answer tough two picture stage. President development call. Establish lead sit plan any.', 'thomaswright@example.com', '001-966-660-2430x1391', 59);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (15, 'Jeffery Wilson', 'Sport campaign interview president improve. Win long apply machine.
Treatment station director check painting red man. Big rest daughter resource agency their here.', 'davidvincent@example.org', '001-667-497-1046x452', 10);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (16, 'Brian Munoz', 'Result north member. Magazine together look why. Back reduce drive late.
Food buy wait young energy now. Success dream ball film north catch site. Lot dog outside style.', 'khanbailey@example.com', '514.863.7711x1001', 13);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (17, 'Abigail Williams', 'She discover training worry. Six participant herself.
Baby ago take democratic hit body high. Federal whole score continue. Direction share perform care federal.', 'scottvaughn@example.org', '+1-202-999-1047', 20);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (18, 'Larry Mullen', 'Support strategy require fund group. Dog join skin fast.
Many apply become family. True detail seem catch within debate wear.', 'daniel49@example.org', '(847)345-0535', 39);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (19, 'Randy Gordon', 'He none worry range give senior. Day all team miss. Up meeting shoulder truth attention group describe.
Product friend until after whole stop. Song make measure admit.', 'rebecca94@example.net', '(548)666-3541x052', 48);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (20, 'Phillip Santana', 'Such radio quite amount rule course.
Animal federal cut hope sell. Fall when top remain wait music ball. In campaign while yes lose medical.
Age former set. Similar happy tree wonder.', 'danielkelly@example.net', '(231)601-4289x7966', 1);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (21, 'Joshua Willis', 'Point home mean enter pull front foot before. Last lay hit international necessary establish discussion.', 'jonathan53@example.org', '366.982.3717', 7);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (22, 'Joy Palmer', 'Near consider defense college. Bit bag maintain after.
Natural other either difference some style civil simple. All structure worry policy. Respond expert miss administration.', 'bensonaimee@example.org', '+1-656-624-1990x149', 2);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (23, 'Cathy Perez', 'Against deal man wall stuff. Until difficult set war. Since action effect task forget mouth parent.
Decade story eight. Interview manage near resource pass blue floor.', 'richardwallace@example.org', '(773)916-3900x56976', 22);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (24, 'Kayla Walton', 'Yard resource build perform upon create mouth. Individual same itself chance change out mind. Traditional cause election explain degree crime book.', 'pcopeland@example.net', '(850)661-7220x81797', 4);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (25, 'Jason Lee', 'Theory boy have dark nation north increase piece. Thousand way morning newspaper wonder through point pattern.', 'andrew35@example.com', '619-810-2009', 7);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (26, 'Monica Warren', 'Everybody these top assume senior time institution. Go kid fire me account eye through affect.
Enjoy note owner charge. Contain hold mean film. Forget him law story deal.', 'wardchristine@example.org', '(316)822-2992', 32);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (27, 'Gilbert Anderson', 'None these third open card discussion. By less manager weight knowledge attorney care. Red especially rule model forward itself discuss energy. Blood church political.
Tonight according hospital.', 'mperry@example.net', '(904)527-4655', 59);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (28, 'Paul Morris', 'Management stop get marriage attack both. Kitchen law yet story.
Other field religious often once something them. Experience no action assume.
Example support friend we have lot billion health.', 'james93@example.org', '+1-477-813-4794x615', 11);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (29, 'Andrea Meyer', 'Author away support and. Maintain past woman. Business kind country price.
Subject artist security million. Everything stage total measure.', 'xgarza@example.net', '001-991-678-7500x787', 13);
INSERT INTO user (userID, name, biography, email, phoneNumber, mood) VALUES (30, 'Jessica Roberson', 'Catch wide after check may possible as. Among simply teacher energy imagine feel. Finish agreement hand receive.
Remain move fish. Point other hear man above.', 'mary33@example.com', '+1-803-313-7288x37179', 9);

-- Generating media types
INSERT INTO mediaType (mediaTypeID, type) VALUES (1, 'Song');
INSERT INTO mediaType (mediaTypeID, type) VALUES (2, 'Book');
INSERT INTO mediaType (mediaTypeID, type) VALUES (3, 'Movie');
