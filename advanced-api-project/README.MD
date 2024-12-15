# Advanced API Project

## Views Configuration

### BookListView

- **URL:** `/books/`
- **Methods:** `GET`, `POST`
- **Description:** Retrieve all books or create a new book.

### BookDetailView

- **URL:** `/books/<int:pk>/`
- **Methods:** `GET`, `PUT`, `DELETE`
- **Description:** Retrieve, update, or delete a book by ID.

### BookCreateView

- **URL:** `/books/create/`
- **Methods:** `POST`
- **Description:** Create a new book instance.

### BookUpdateView

- **URL:** `/books/<int:pk>/update/`
- **Methods:** `PUT`
- **Description:** Update an existing book instance.

### BookDeleteView

- **URL:** `/books/<int:pk>/delete/`
- **Methods:** `DELETE`
- **Description:** Delete a book instance.

## Permissions

- **BookCreateView, BookUpdateView, BookDeleteView:** Restricted to authenticated users only.
- **BookListView, BookDetailView:** Read-only access allowed for unauthenticated users.

## Testing

Manually test each view using tools like Postman or `curl` to ensure they function as expected and permissions are enforced correctly.
