export const getPosts = async function getPosts() {
  let url = `http://127.0.0.1:5000/entry`;
  const response = await fetch(url);
  let data = await response.json();

  return data;
};

export const createPost = async function createPost(
  post_title = "",
  post_date = "",
  post_content = ""
) {
  console.log(
    ` create post ${post_title} and ${post_date} and ${post_content}`
  );
  let url = `http://127.0.0.1:5000/add`;
  const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      title: post_title,
      date: post_date,
      content: post_content,
    }),
  };

  fetch(url, requestOptions).then(console.log("created"));
};

export const readPost = async function retrievePost(id = undefined) {
  if (!id) return getPosts;

  let url = `http://127.0.0.1:5000/entry/${id}`;
  const response = await fetch(url);
  let data = await response.json();

  return data;
};

export const updatePost = async function updatePost(
  post_id = "",
  post_title = "",
  post_content = ""
) {
  if (!post_id) return;
  console.log(` update post ${post_id}. ${post_title} and ${post_content}`);
  let url = `http://127.0.0.1:5000/edit`;
  const requestOptions = {
    method: "PUT",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      id: post_id,
      title: post_title,
      content: post_content,
    }),
  };
  fetch(url, requestOptions).then(console.log("updated"));
};

export const deletePost = async function deletePost(id = undefined) {
  if (!id) return;

  let url = `http://127.0.0.1:5000/delete/${id}`;
  fetch(url).then(console.log("deleted"));
};
