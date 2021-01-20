import React from "react";
import { Button } from "react-bootstrap";

function EditButton(props) {
  const { editClick, updateClick, isEdit } = props;

  if (isEdit)
    return (
      <Button variant="info" onClick={updateClick}>
        Update
      </Button>
    );
  else
    return (
      <Button variant="warning" onClick={editClick}>
        Edit
      </Button>
    );
}

export default EditButton;
