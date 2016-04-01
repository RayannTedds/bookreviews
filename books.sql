PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE genre (
genreID INT NOT NULL PRIMARY KEY,
genre VARCHAR(60) NOT NULL);
INSERT INTO "genre" VALUES(1000,'Fiction');
INSERT INTO "genre" VALUES(1001,'Chick Lit');
INSERT INTO "genre" VALUES(1002,'Historical Fiction');
INSERT INTO "genre" VALUES(1004,'Classics');
CREATE TABLE author (
authorID INT NOT NULL PRIMARY KEY,
forename VARCHAR(100) NOT NULL,
surname VARCHAR(100) NOT NULL);
INSERT INTO "author" VALUES(1,'Harper','Lee');
INSERT INTO "author" VALUES(2,'Sophie','Kinsella');
INSERT INTO "author" VALUES(3,'Madeleine','Wickham');
INSERT INTO "author" VALUES(4,'Khaled','Hosseini');
INSERT INTO "author" VALUES(5,'F. Scott','Fitzgerald');
INSERT INTO "author" VALUES(6,'Jonathan','Harvey');
CREATE TABLE awards (
awardGroupID CHAR(2) NOT NULL PRIMARY KEY,
award1 VARCHAR2(255) NOT NULL,
award2 VARCHAR(255),
award3 VARCHAR(255),
award4 VARCHAR(255),
award5 VARCHAR(255),
award6 VARCHAR(255),
award7 VARCHAR(255),
award8 VARCHAR(255),
award9 VARCHAR(255),
award10 VARCHAR(255));
INSERT INTO "awards" VALUES('a','None',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "awards" VALUES('b','Goodreads Choice Award Best Fiction',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "awards" VALUES('c','Literature to Life Award','San Francisco Chronicle Best Book of the Year','Entertainment Weekly - Best Book','Borders Original Voices Award','Alex Award','ALA Notable Book','Barnes and Noble Discover Great New Writers Award','Boeke Prize','Book Sense Bestseller List Sensation','Penguin/Orange Readers Group Prize');
CREATE TABLE book (
bookID INT NOT NULL PRIMARY KEY,
name VARCHAR(200) NOT NULL,
published DATE NOT NULL,
authorID INT NOT NULL,
genreID INT NOT NULL,
awardGroupID CHAR(2) NOT NULL,
myReview TEXT NOT NULL,
myReviewDate DATE NOT NULL,
review1 TEXT,
review2 TEXT,
review3 TEXT,
review4 TEXT,
review5 TEXT,
review6 TEXT,
review7 TEXT,
review8 TEXT,
review9 TEXT,
review10 TEXT,
FOREIGN KEY(authorID) REFERENCES author(authorID),
FOREIGN KEY(genreID) REFERENCES genre(genreID),
FOREIGN KEY(awardGroupID) REFERENCES awards(awardGroupID));
INSERT INTO "book" VALUES(1000000,'Go Set A Watchman',2015,1,1000,'b','Spoiler Alert! It was so nice being back in the distinct voice of Harper Lee and Jean-Louise (Scout) Finch after reading To Kill A Mockingbird about 5 years ago. Still, to this day, it remains one of my favourite books. Go Set A Watchman is a very nice sequel to the book however, I did feel that there was not a lot of substance in it when its compared with its companion book. The book is about Jean-Louise learning about her own conscience and that is about it, wish there was more going on in the storyline but still a nice read.3/5 stars because of the lack of twists and turns compared to To Kill A Mockingbird.',-2002,'A new work, and a pleasure, revelation and genuine literacy event... This publication intensified the regret that Harper Lee published so little.','The more radical, ambitious and politicised of the two novels Lee has now published... It is a book of enormous literacy interest... Beguiling and distinctive.''More edgy and thought provoking thanTo Kill A Mockingbird]... There is the  Lee trademark warmth... [It has] a surprisingly provactive message - do not airily dismiss the prejudices of others, try to understand them.','Reacquaint yourself with that beguiling Harper Lee narrative style - warm, sardonic, amused... wryly funny, a sassy Southern voice, Mark Twain with a dash of Katherine Hepburn.','Feminist and wickedly modern.','A powerful and moving novel... It is a worthy successor.','Fascinating, haunting... That voice remains the same: strong, humorous, unsentimental; the unmistakable voice of Harper Lee... The mockingbird still sings... a song that combines sorrow, forgiveness - and, ultimately, a kind of hope.',NULL,NULL,NULL,NULL);
INSERT INTO "book" VALUES(1000001,'Shopaholic on Honeymoon',2014,2,1001,'a','After reading all the shopaholic books, I was starting to get bored of the same plots each time. However, I randomly came across the free kindle edition of this mini book and decided to read it and I am absolutely gutted that it was not  a full novel, I could see real potential in this, so much more so then Shopaholic to the Stars. It got me excited to travel the world.',2016,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "book" VALUES(1000002,'Cocktails For Three',2000,3,1001,'a','To be honest, I really like the idea of switching between personalities for each of the chapters, and for me, this was the best part of the book. I have loved this author for many years but I found this book a little dry and slow, it had a few good points do not get me wrong - it could have been that I felt this way due to the fact I read it 5 years after it was published and so the technology side was a bit behind. Unfortunately, the book did not excite me and so this is the reason for my low review. We have all been through situations like this in life and I felt that the story was overly drawn out when it could have been a shorter story getting to the heart of the problem.',2015,'A new work, and a pleasure, revelation and genuine literacy event... This publication intensified the regret that Harper Lee published so little.',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "book" VALUES(1000003,'The Kite Runner',2003,4,1002,'c','This book is truly eye - opening and a great read. It is not the typical book I would pick up to read and yet it was a pleasure to read and I found that I learnt a lot about different cultures and ideas of the world. It made me feel as though there as so much more to learn in the world, particularly about other countries and how they came to be the environments they are today, like in Afghanistan. A recommended read, definitely.',2015,'A devastating, masterful and painfully honest story','A novel of unusual generosity, honesty and compassion.','Shattering ... devastating and inspiring.','Unforgettable ... extraordinary. It is so powerful that for a long time after, everything I read seemed bland.','A marvellous first novel ... It is an old-fashioned kind of novel that really sweeps you away.','Stunning ... It is rare that a book is at once so timely and of such high literary quality','Balances socio-political commentary with an emotionally powerful narrative','Here is a real find: a striking debut... a passionate story of betrayal and redemption ... a searing spectacle of hard-won personal salvation. All this, and a rich slice of Afghan culture too: irresistable.','It is remarkable. It is like a condensed history of Afghanistan, mixed with a Shakespearean tale of friendship and love ... brilliant','What is most conspicuous on almost every page of this debut is not language, but the shimmer of life. There is no display in Hosseinis  writing, only expression - a lession for all budding novelists ... Hosseini does tenderness and terror, California dream and Kabul nightmare with equal aplomb ... A carefully built structure of ripping yarn andethical parable.');
INSERT INTO "book" VALUES(1000005,'The Secrets We Keep',2015,6,1,'a','I actually really enjoyed this book. Calmly reminded me of how my friends and I must have been at that annoying ages and it really did make me chuckle. It is a different kind of story to what I have read before and thought it was great. Love the transition of characters each chapter. The ending has, however, made me want to know more about what happened next!',2015,'A wonderful book - gripping and twisty and tender and touching.','Absolutely delightful. Jonathan Harvey writes with all his heart and with all his soul.',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
INSERT INTO "book" VALUES(1000004,'The Great Gatsby',1925,5,1003,'a','I loved the historical element to this book and the love interest twist within this book however, following on from this, I really did not feel like much actually happened within the book unfortunately. After the hype of the film, I was left disappointed with the book.',2015,'The Great Gatsby is in many ways similar to Romeo and Juliet yet it is so much more than a love story.','Book of a lifetime: melancholy, and unforgettable melody.',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL);
COMMIT;
