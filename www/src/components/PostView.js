import React, { useState } from "react";
import { Button, Form, Modal, ListGroup } from "react-bootstrap";
import { Input } from "reactstrap";

import { deletePost, updatePost } from "../api/BlogCommands";
import EditButton from "./EditButton";

function PostView(props) {
  const { title, date, id, content } = props;
  const [show, setShow] = useState(false);
  const [isEdit, setIsEdit] = useState(false);
  const [postTitle, setPostTitle] = useState(title);
  const [postContent, setPostContent] = useState(content);

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
    console.log(`Updating: ${id}`);
    updatePost(id, postTitle, postContent);
    handleClose();
  };
  const dateFmt = (inputInstant) => {
    const dte = new Date(inputInstant);
    const year = dte.getFullYear();
    const month = (dte.getMonth() + 1).toString().padStart(2, "0");
    const day = dte.getDate().toString().padStart(2, "0");

    return `${year}-${month}-${day}`;
  };

  return (
    <>
      <ListGroup.Item action id={id} onClick={handleShow}>
        {`${id}. ${title}`}
      </ListGroup.Item>

      <Modal show={show} onHide={handleClose} centered>
        <Modal.Body>
          <Form>
            <Form.Control
              onChange={(e) => {
                setPostTitle(e.target.value);
              }}
              placeholder="Title"
              value={postTitle}
              disabled={!isEdit}
            />
            <br />
            <Input
              type="date"
              placeholder="choose a date"
              value={dateFmt(date)}
              disabled
            />
            <br />
            <Form.Control
              as="textarea"
              onChange={(e) => {
                setPostContent(e.target.value);
              }}
              placeholder="Text (optional)"
              rows={3}
              value={postContent}
              disabled={!isEdit}
            />
          </Form>
        </Modal.Body>
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
