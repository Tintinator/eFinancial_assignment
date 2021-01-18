import React, { useState } from "react";
import { Button, Form, Modal } from "react-bootstrap";
import "../styles/NewEntry.css";

function NewEntry() {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  return (
    <>
      <Button variant="outline-dark" size="lg" onClick={handleShow}>
        New Blog Post
      </Button>

      <Modal show={show} onHide={handleClose}>
        <Modal.Header closeButton>
          <Modal.Title>Create a Post</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Form>
            <Form.Control className="Form" placeholder="Title" />
            <br />
            <Form.Control className="Form" placeholder="Date" />
            <br />
            <Form.Control
              className="Form"
              as="textarea"
              placeholder="Text (optional)"
              rows={3}
            />
          </Form>
        </Modal.Body>
        <Modal.Footer>
          <Button variant="secondary" onClick={handleClose}>
            Cancel
          </Button>
          <Button variant="primary" onClick={handleClose}>
            Publish
          </Button>
        </Modal.Footer>
      </Modal>
    </>
  );
}

export default NewEntry;
