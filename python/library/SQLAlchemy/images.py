# -*- encoding: utf-8 -*-

"""
http://bytefish.de/blog/first_steps_with_sqlalchemy/

An image consist of a UUID and its associated number of likes. Each image can
be associated with many tags, a tag can be associated with many images. That's
a many-to-many relationship, so we need a mapping table. Finally each image
can have multiple comments, a one-to-many relation with a foreign key on
the comments side.
"""

# Model
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from datetime import datetime, timedelta
from sqlalchemy import Table, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship, backref

images_tags = Table(
    'images_tags', Base.metadata,
    Column('image_id', Integer, ForeignKey('images.id')),
    Column('tag_id', Integer, ForeignKey('tags.id')),
)

class Image(Base):

    __tablename__ = 'images'

    id          =   Column(Integer, primary_key=True)
    uuid        =   Column(String(36), unique=True, nullable=False)
    likes       =   Column(Integer, default=0)
    created_at  =   Column(DateTime, default=datetime.utcnow)
    tags        =   relationship('Tag', secondary=images_tags, 
                        backref = backref('images', lazy='dynamic'))
    comments    =   relationship('Comment', backref='image', lazy='dynamic')

    def __repr__(self):
        str_created_at = self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        return "<Image (uuid='%s', likes='%d', created_at=%s)>" % (self.uuid, self.likes, str_created_at)

class Tag(Base):

    __tablename__ = 'tags'

    id      =   Column(Integer, primary_key=True)
    name    =   Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return "<Tag (name='%s')>" % (self.name)

class Comment(Base):

    __tablename__ = 'comments'

    id          =   Column(Integer, primary_key=True)
    text        =   Column(String(2000))
    image_id    =   Column(Integer, ForeignKey('images.id'))

    def __repr__(self):
        return "<Comment (text='%s')>" % (self.text)

# Connecting and Creating the Schema
from sqlalchemy import create_engine

engine = create_engine('sqlite:///images.db', echo=True)
# in-memory
#engine = create_engine('sqlite://', echo=True)

Base.metadata.create_all(engine)

"""
$ python images.py
2016-04-18 15:15:54,754 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2016-04-18 15:15:54,754 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,754 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2016-04-18 15:15:54,754 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,756 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images")
2016-04-18 15:15:54,756 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,756 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images_tags")
2016-04-18 15:15:54,756 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,756 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("comments")
2016-04-18 15:15:54,757 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,757 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("tags")
2016-04-18 15:15:54,757 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,758 INFO sqlalchemy.engine.base.Engine
CREATE TABLE images (
        id INTEGER NOT NULL,
        uuid VARCHAR(36) NOT NULL,
        likes INTEGER,
        created_at DATETIME,
        PRIMARY KEY (id),
        UNIQUE (uuid)
)


2016-04-18 15:15:54,758 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,760 INFO sqlalchemy.engine.base.Engine COMMIT
2016-04-18 15:15:54,760 INFO sqlalchemy.engine.base.Engine
CREATE TABLE tags (
        id INTEGER NOT NULL,
        name VARCHAR(255) NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (name)
)


2016-04-18 15:15:54,760 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,762 INFO sqlalchemy.engine.base.Engine COMMIT
2016-04-18 15:15:54,762 INFO sqlalchemy.engine.base.Engine
CREATE TABLE images_tags (
        image_id INTEGER,
        tag_id INTEGER,
        FOREIGN KEY(image_id) REFERENCES images (id),
        FOREIGN KEY(tag_id) REFERENCES tags (id)
)


2016-04-18 15:15:54,762 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,764 INFO sqlalchemy.engine.base.Engine COMMIT
2016-04-18 15:15:54,764 INFO sqlalchemy.engine.base.Engine
CREATE TABLE comments (
        id INTEGER NOT NULL,
        text VARCHAR(2000),
        image_id INTEGER,
        PRIMARY KEY (id),
        FOREIGN KEY(image_id) REFERENCES images (id)
)


2016-04-18 15:15:54,764 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:15:54,766 INFO sqlalchemy.engine.base.Engine COMMIT
"""

# Sessions
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)

session = Session()

# Insert
tag_cool = Tag(name='cool')
tag_car = Tag(name='car')
tag_animal = Tag(name='animal')

comment_rhino = Comment(text='Rhinoceros, often abbreviated as rhino, is a group of five extant species of odd-toed ungulates in the family Rhinocerotidae.')

image_car = Image(uuid='uuid_car', \
    tags=[tag_car, tag_cool], \
    created_at=(datetime.utcnow() - timedelta(days=1)))

image_another_car = Image(uuid='uuid_anothercar', \
    tags=[tag_car])

image_rhino = Image(uuid='uuid_rhino', \
    tags=[tag_animal], \
    comments=[comment_rhino])

# run once because of unique
# session.add(tag_cool)
# session.add(tag_car)
# session.add(tag_animal)

# session.add(comment_rhino)

# session.add(image_car)
# session.add(image_another_car)
# session.add(image_rhino)

# session.commit()

"""
$ python images.py
2016-04-18 15:23:10,787 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2016-04-18 15:23:10,787 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:23:10,788 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2016-04-18 15:23:10,788 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:23:10,789 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images")
2016-04-18 15:23:10,789 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:23:10,790 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images_tags")
2016-04-18 15:23:10,790 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:23:10,790 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("comments")
2016-04-18 15:23:10,790 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:23:10,790 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("tags")
2016-04-18 15:23:10,790 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:23:10,802 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2016-04-18 15:23:10,803 INFO sqlalchemy.engine.base.Engine INSERT INTO images (uuid, likes, created_at) VALUES (?, ?, ?)
2016-04-18 15:23:10,803 INFO sqlalchemy.engine.base.Engine ('uuid_car', 0, '2016-04-17 07:23:10.798788')
2016-04-18 15:23:10,804 INFO sqlalchemy.engine.base.Engine INSERT INTO images (uuid, likes, created_at) VALUES (?, ?, ?)
2016-04-18 15:23:10,804 INFO sqlalchemy.engine.base.Engine ('uuid_anothercar', 0, '2016-04-18 07:23:10.804351')
2016-04-18 15:23:10,804 INFO sqlalchemy.engine.base.Engine INSERT INTO images (uuid, likes, created_at) VALUES (?, ?, ?)
2016-04-18 15:23:10,804 INFO sqlalchemy.engine.base.Engine ('uuid_rhino', 0, '2016-04-18 07:23:10.804775')
2016-04-18 15:23:10,805 INFO sqlalchemy.engine.base.Engine INSERT INTO tags (name) VALUES (?)
2016-04-18 15:23:10,805 INFO sqlalchemy.engine.base.Engine ('cool',)
2016-04-18 15:23:10,806 INFO sqlalchemy.engine.base.Engine INSERT INTO tags (name) VALUES (?)
2016-04-18 15:23:10,806 INFO sqlalchemy.engine.base.Engine ('car',)
2016-04-18 15:23:10,806 INFO sqlalchemy.engine.base.Engine INSERT INTO tags (name) VALUES (?)
2016-04-18 15:23:10,806 INFO sqlalchemy.engine.base.Engine ('animal',)
2016-04-18 15:23:10,807 INFO sqlalchemy.engine.base.Engine INSERT INTO images_tags (image_id, tag_id) VALUES (?, ?)
2016-04-18 15:23:10,807 INFO sqlalchemy.engine.base.Engine ((1, 2), (1, 1), (2, 2), (3, 3))
2016-04-18 15:23:10,808 INFO sqlalchemy.engine.base.Engine INSERT INTO comments (text, image_id) VALUES (?, ?)
2016-04-18 15:23:10,808 INFO sqlalchemy.engine.base.Engine ('Rhinoceros, often abbreviated as rhino, is a group of five extant species of odd-toed ungulates in the family Rhinocerotidae.', 3)
2016-04-18 15:23:10,809 INFO sqlalchemy.engine.base.Engine COMMIT
"""

# Update
# Find the image with the given uuid:
image_to_update = session.query(Image).filter(Image.uuid == 'uuid_rhino').first()
# Increase the number of upvotes:
image_to_update.likes = image_to_update.likes + 1
# And commit the work:
session.commit()

"""
$ python images.py
2016-04-18 15:46:26,587 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2016-04-18 15:46:26,587 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:46:26,588 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2016-04-18 15:46:26,588 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:46:26,589 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images")
2016-04-18 15:46:26,589 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:46:26,590 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images_tags")
2016-04-18 15:46:26,590 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:46:26,590 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("comments")
2016-04-18 15:46:26,590 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:46:26,591 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("tags")
2016-04-18 15:46:26,591 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 15:46:26,601 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2016-04-18 15:46:26,602 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images
WHERE images.uuid = ?
 LIMIT ? OFFSET ?
 2016-04-18 15:46:26,602 INFO sqlalchemy.engine.base.Engine ('uuid_rhino', 1, 0)
 2016-04-18 15:46:26,604 INFO sqlalchemy.engine.base.Engine UPDATE images SET likes=? WHERE images.id = ?
 2016-04-18 15:46:26,604 INFO sqlalchemy.engine.base.Engine (1, 3)
 2016-04-18 15:46:26,605 INFO sqlalchemy.engine.base.Engine COMMIT
"""

# Queries
# Get a list of tags:
for name in session.query(Tag.name).order_by(Tag.name):
        print name
"""
$ python images.py
2016-04-18 16:06:45,831 INFO sqlalchemy.engine.base.Engine SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
2016-04-18 16:06:45,832 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 16:06:45,832 INFO sqlalchemy.engine.base.Engine SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
2016-04-18 16:06:45,832 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 16:06:45,833 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images")
2016-04-18 16:06:45,833 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 16:06:45,834 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("images_tags")
2016-04-18 16:06:45,834 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 16:06:45,835 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("comments")
2016-04-18 16:06:45,835 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 16:06:45,835 INFO sqlalchemy.engine.base.Engine PRAGMA table_info("tags")
2016-04-18 16:06:45,835 INFO sqlalchemy.engine.base.Engine ()
2016-04-18 16:06:45,845 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2016-04-18 16:06:45,846 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images
WHERE images.uuid = ?
 LIMIT ? OFFSET ?
2016-04-18 16:06:45,846 INFO sqlalchemy.engine.base.Engine ('uuid_rhino', 1, 0)
2016-04-18 16:06:45,848 INFO sqlalchemy.engine.base.Engine UPDATE images SET likes=? WHERE images.id = ?
2016-04-18 16:06:45,848 INFO sqlalchemy.engine.base.Engine (10, 3)
2016-04-18 16:06:45,849 INFO sqlalchemy.engine.base.Engine COMMIT
2016-04-18 16:06:45,852 INFO sqlalchemy.engine.base.Engine BEGIN (implicit)
2016-04-18 16:06:45,853 INFO sqlalchemy.engine.base.Engine SELECT tags.name AS tags_name
FROM tags ORDER BY tags.name
2016-04-18 16:06:45,853 INFO sqlalchemy.engine.base.Engine ()
(u'animal',)
(u'car',)
(u'cool',)
"""

# How many tags do we have?
print session.query(Tag).count()
"""
2016-04-18 16:10:09,912 INFO sqlalchemy.engine.base.Engine SELECT count(*) AS count_1
FROM (SELECT tags.id AS tags_id, tags.name AS tags_name
FROM tags) AS anon_1
2016-04-18 16:10:09,912 INFO sqlalchemy.engine.base.Engine ()
3
"""

# Get all images created yesterday:
print session.query(Image) \
    .filter(Image.created_at < datetime.utcnow().date()) \
    .all()
"""
2016-04-18 16:10:09,914 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images
WHERE images.created_at < ?
2016-04-18 16:10:09,914 INFO sqlalchemy.engine.base.Engine ('2016-04-18',)
[<Image (uuid='uuid_car', likes='0', created_at=2016-04-17 07:23:10)>]
"""

# Get all images, that belong to the tag 'car' or 'animal', using a subselect:
print session.query(Image) \
    .filter(Image.tags.any(Tag.name.in_(['car', 'animal']))) \
    .all()
"""
2016-04-18 16:10:09,917 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images
WHERE EXISTS (SELECT 1
FROM images_tags, tags
WHERE images.id = images_tags.image_id AND tags.id = images_tags.tag_id AND tags.name IN (?, ?))
2016-04-18 16:10:09,917 INFO sqlalchemy.engine.base.Engine ('car', 'animal')
[<Image (uuid='uuid_car', likes='0', created_at=2016-04-17 07:23:10)>, <Image (uuid='uuid_anothercar', likes='0', created_at=2016-04-18 07:23:10)>, <Image (uuid='uuid_rhino', likes='12', created_at=2016-04-18 07:23:10)>]
"""

# This can also be expressed with a join:
print session.query(Image) \
    .join(Tag, Image.tags) \
    .filter(Tag.name.in_(['car', 'animal'])) \
    .all()
"""
2016-04-18 16:10:09,920 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images JOIN images_tags AS images_tags_1 ON images.id = images_tags_1.image_id JOIN tags ON tags.id = images_tags_1.tag_id
WHERE tags.name IN (?, ?)
2016-04-18 16:10:09,920 INFO sqlalchemy.engine.base.Engine ('car', 'animal')
[<Image (uuid='uuid_car', likes='0', created_at=2016-04-17 07:23:10)>, <Image (uuid='uuid_anothercar', likes='0', created_at=2016-04-18 07:23:10)>, <Image (uuid='uuid_rhino', likes='12', created_at=2016-04-18 07:23:10)>]
"""

# Play around with functions:
from sqlalchemy.sql import func, desc

max_date = session.query(func.max(Image.created_at))
print session.query(Image).filter(Image.created_at == max_date).first()
"""
2016-04-18 16:10:09,922 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images
WHERE images.created_at = (SELECT max(images.created_at) AS max_1
FROM images)
 LIMIT ? OFFSET ?
2016-04-18 16:10:09,922 INFO sqlalchemy.engine.base.Engine (1, 0)
<Image (uuid='uuid_rhino', likes='12', created_at=2016-04-18 07:23:10)>
"""

# Get a list of tags with the number of images:
q = session.query(Tag, func.count(Tag.name)) \
    .outerjoin(Image, Tag.images) \
    .group_by(Tag.name) \
    .order_by(desc(func.count(Tag.name))) \
    .all()

for tag, count in q:
    print 'Tag "%s" has %d images.' % (tag.name, count) 
"""
2016-04-18 16:10:09,927 INFO sqlalchemy.engine.base.Engine SELECT tags.id AS tags_id, tags.name AS tags_name, count(tags.name) AS count_1
FROM tags LEFT OUTER JOIN (SELECT images_tags_1.image_id AS images_tags_1_image_id, images_tags_1.tag_id AS images_tags_1_tag_id, images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images_tags AS images_tags_1 JOIN images ON images.id = images_tags_1.image_id) AS anon_1 ON tags.id = anon_1.images_tags_1_tag_id GROUP BY tags.name ORDER BY count(tags.name) DESC
2016-04-18 16:10:09,928 INFO sqlalchemy.engine.base.Engine ()
Tag "car" has 2 images.
Tag "animal" has 1 images.
Tag "cool" has 1 images.
"""

# Get images created in the last two hours and zero likes so far:
print session.query(Image) \
    .join(Tag, Image.tags) \
    .filter(Image.created_at > (datetime.utcnow() - timedelta(hours=2))) \
    .filter(Image.likes == 0) \
    .all()
"""
2016-04-18 16:10:09,930 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images JOIN images_tags AS images_tags_1 ON images.id = images_tags_1.image_id JOIN tags ON tags.id = images_tags_1.tag_id
WHERE images.created_at > ? AND images.likes = ?
2016-04-18 16:10:09,931 INFO sqlalchemy.engine.base.Engine ('2016-04-18 06:10:09.929513', 0)
[<Image (uuid='uuid_anothercar', likes='0', created_at=2016-04-18 07:23:10)>]
"""

# Delete
print '@@@ Delete'
image_rhino = session.query(Image).filter(Image.uuid == 'uuid_rhino').first()
print image_rhino
session.delete(image_rhino)
session.commit()
"""
@@@ Delete
2016-04-18 16:36:55,016 INFO sqlalchemy.engine.base.Engine SELECT images.id AS images_id, images.uuid AS images_uuid, images.likes AS images_likes, images.created_at AS images_created_at
FROM images
WHERE images.uuid = ?
 LIMIT ? OFFSET ?
2016-04-18 16:36:55,016 INFO sqlalchemy.engine.base.Engine ('uuid_rhino', 1, 0)
<Image (uuid='uuid_rhino', likes='18', created_at=2016-04-18 07:23:10)>
2016-04-18 16:36:55,018 INFO sqlalchemy.engine.base.Engine SELECT comments.id AS comments_id, comments.text AS comments_text, comments.image_id AS comments_image_id
FROM comments
WHERE ? = comments.image_id
2016-04-18 16:36:55,018 INFO sqlalchemy.engine.base.Engine (3,)
2016-04-18 16:36:55,020 INFO sqlalchemy.engine.base.Engine SELECT tags.id AS tags_id, tags.name AS tags_name
FROM tags, images_tags
WHERE ? = images_tags.image_id AND tags.id = images_tags.tag_id
2016-04-18 16:36:55,020 INFO sqlalchemy.engine.base.Engine (3,)
2016-04-18 16:36:55,021 INFO sqlalchemy.engine.base.Engine DELETE FROM images_tags WHERE images_tags.image_id = ? AND images_tags.tag_id = ?
2016-04-18 16:36:55,021 INFO sqlalchemy.engine.base.Engine (3, 3)
2016-04-18 16:36:55,022 INFO sqlalchemy.engine.base.Engine UPDATE comments SET image_id=? WHERE comments.id = ?
2016-04-18 16:36:55,023 INFO sqlalchemy.engine.base.Engine (None, 1)
2016-04-18 16:36:55,023 INFO sqlalchemy.engine.base.Engine DELETE FROM images WHERE images.id = ?
2016-04-18 16:36:55,023 INFO sqlalchemy.engine.base.Engine (3,)
2016-04-18 16:36:55,024 INFO sqlalchemy.engine.base.Engine COMMIT
"""

