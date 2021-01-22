import React, { useState } from "react";
import { Button, Form, Modal } from "react-bootstrap";
import { Input } from "reactstrap";

import "../styles/NewEntry.css";
import { createPost } from "../api/BlogCommands";

function NewEntry() {
  const [title, setTitle] = React.useState("");
  const [date, setDate] = React.useState("");
  const [content, setContent] = React.useState("");
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);
  const publishPost = () => {
    createPost(title, date, content);
    handleClose();
  };

  return (
    <>
      <Button variant="outline-dark" size="lg" onClick={handleShow}>
        New Blog Post
      </Button>

      <Modal show={show} onHide={handleClose} centered>
        <Modal.Header closeButton>
          <Modal.Title>Create a Post</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Control
              onChange={(e) => {
                setTitle(e.target.value);
              }}
              placeholder="Title"
            />
            <br />
            <Input
              type="date"
              name="customDate"
              placeholder="choose a date"
              onChange={(e) => {
                setDate(e.target.value);
              }}
              value={date}
            />
            <br />
            <Form.Control
              as="textarea"
              onChange={(e) => {
                setContent(e.target.value);
              }}
              placeholder="Text (optional)"
              rows={3}
            />
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Cancel
          </Button>
          <Button variant="primary" onClick={publishPost}>
            Publish
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default NewEntry;
