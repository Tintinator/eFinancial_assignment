import React from "react";
import { ListGroup } from "react-bootstrap";

import PostView from "./PostView";

function PostList(props) {
  const { data, isFetching } = props;

  return (
    <div>
      <ListGroup>
        <ListGroup.Item action href="#link1">
          Link 1
        </ListGroup.Item>
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

      <p>{isFetching ? "Fetching posts..." : ""}</p>
    </div>
  );
}

export default PostList;
