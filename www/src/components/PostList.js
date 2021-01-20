import React from "react";
import { Card, ListGroup } from "react-bootstrap";

import PostView from "./PostView";

function PostList(props) {
  const { data, isFetching } = props;

  return (
    <div>
      <Card>
        <Card.Header>Posts</Card.Header>
        <ListGroup variante="flush">
          {data &&
            data.map((entryObj) => (
              <PostView
                key={entryObj.entry_id}
                title={entryObj.entry_title}
                date={entryObj.entry_date}
                id={entryObj.entry_id}
                content={entryObj.entry_content}
              />
            ))}
        </ListGroup>
      </Card>

      <p>{isFetching ? "Fetching posts..." : ""}</p>
    </div>
  );
}

export default PostList;
