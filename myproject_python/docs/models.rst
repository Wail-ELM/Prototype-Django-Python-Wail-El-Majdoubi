Models
======

This module defines the data models for the blog application.

.. automodule:: blog.models
   :members:

Article Model
-------------

The `Article` model represents a blog post and has the following fields:

*  `title`: The title of the post (CharField).
*  `content`: The content of the post (TextField).
*  `author`: The author of the post (ForeignKey to User).
*  `created_at`: The date and time the post was created (DateTimeField).