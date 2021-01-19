import React, { useState } from "react";
import { Button, Form, Modal, ListGroup } from "react-bootstrap";
import { Input } from "reactstrap";

import { deletePost, updatePost } from "../api/BlogCommands";
import EditButton from "./EditButton";

function PostView(props) {
  const [show, setShow] = useState(false);
  const [isEdit, setIsEdit] = useState(false);
  const { title, date, id, content } = props;

  const handleClose = () => setShow(false);
  const handleShow = () => {
    handleView();
    setShow(true);
  };
  const handleEdit = () => setIsEdit(true);
  const handleView = () => setIsEdit(false);
  const handleDelete = () => {
    console.log(`Deleting: ${id}`);
    deletePost(id);
    handleClose();
  };
  const handleUpdate = () => {
    console.log("temp update");
  };

  return (
    <>
      <ListGroup.Item action id={id} onClick={handleShow}>
        {`${id}. ${title}`}
      </ListGroup.Item>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          {/* probably make a div here with like ended inputs for date */}
          <Modal.Title>{`${id}. ${title}`}</Modal.Title>
        </Modal.Header>
        <Modal.Body>{content}</Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <EditButton
            editClick={handleEdit}
            updateClick={handleUpdate}
            isEdit={isEdit}
          />
          <Button variant="danger" onClick={handleDelete}>
            Delete
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default PostView;
