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

  fetch(url, requestOptions).then(console.log("done"));
};
