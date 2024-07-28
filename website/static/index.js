//send requests. Takes passed note id and sends POST request to deleteNote end point then
// reloads the window and redirects to home page(refreshes page in this case since there's only 1 page )
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }