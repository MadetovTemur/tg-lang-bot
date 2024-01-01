# -*- coding: utf-8 -*-

users = """
CREATE TABLE IF NOT EXISTS "users" (
  "user_id"	INTEGER UNIQUE,
  "username"	TEXT DEFAULT NULL,
  "startime"	TEXT,
  "status"	TEXT DEFAULT NULL,
  "chat_lang"	TEXT ,
  "oldtime"	TEXT
);"""

quotes = """
CREATE TABLE IF NOT EXISTS "quotes" (
  "id"	INTEGER NOT NULL UNIQUE,
  "message"	TEXT,
  "message_author"	INTEGER,
  "text_author"	TEXT,
  "is_send"	TEXT DEFAULT NULL,
  "status"	TEXT DEFAULT NULL,
  PRIMARY KEY("id" AUTOINCREMENT)
);
"""

admins = """
CREATE TABLE IF NOT EXISTS  "admins" (
  "admin_id"	INTEGER NOT NULL UNIQUE,
  "user_id"	INTEGER,
  "status"	TEXT DEFAULT 'True',
  PRIMARY KEY("admin_id" AUTOINCREMENT)
);
"""
