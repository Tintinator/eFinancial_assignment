import React from "react";
import { Button, Form, Modal, ListGroup } from "react-bootstrap";
import { Input } from "reactstrap";

import { deletePost, updatePost } from "../api/BlogCommands";
import EditButton from "./EditButton";

class PostView extends React.Component {
  constructor(props) {
    super(props);
    const { title, content } = this.props;
    this.state = {
      show: false,
      isEdit: false,
      postTitle: title,
      postContent: content,
    };
  }

  handleClose = () => this.setState({ ...this.state, show: false });

  handleShow = () => {
    this.handleView();
    this.setState({ ...this.state, show: true });
  };

  handleEdit = () => this.setState({ ...this.state, isEdit: true });

  handleView = () => this.setState({ ...this.state, isEdit: false });

  handleDelete = () => {
    const { id } = this.props;

    console.log(`Deleting: ${id}`);
    deletePost(id);
    this.handleClose();
  };

  handleUpdate = () => {
    const { id } = this.props;
    const { postTitle, postContent } = this.state;

    console.log(`Updating: ${id}`);
    updatePost(id, postTitle, postContent);
    this.handleClose();
  };

  dateFmt = (inputInstant) => {
    const dte = new Date(inputInstant);
    const year = dte.getFullYear();
    const month = (dte.getMonth() + 1).toString().padStart(2, "0");
    const day = dte.getDate().toString().padStart(2, "0");

    return `${year}-${month}-${day}`;
  };

  render() {
    const { id, date } = this.props;
    const { isEdit, show, postTitle, postContent } = this.state;

    return (
      <>
        <ListGroup.Item action id={id} onClick={this.handleShow}>
          {`${id}. ${postTitle}`}
        </ListGroup.Item>

        <Modal show={show} onHide={this.handleClose} centered>
          <Modal.Body>
            <Form>
              <Form.Control
                onChange={(e) => {
                  this.setState({ ...this.state, postTitle: e.target.value });
                }}
                placeholder="Title"
                value={postTitle}
                disabled={!isEdit}
              />
              <br />
              <Input
                type="date"
                placeholder="choose a date"
                value={this.dateFmt(date)}
                disabled
              />
              <br />
              <Form.Control
                as="textarea"
                onChange={(e) => {
                  this.setState({ ...this.state, postContent: e.target.value });
                }}
                placeholder="Text (optional)"
                rows={3}
                value={postContent}
                disabled={!isEdit}
              />
            </Form>
          </Modal.Body>
          <Modal.Footer>
            <Button variant="secondary" onClick={this.handleClose}>
              Close
            </Button>
            <EditButton
              editClick={this.handleEdit}
              updateClick={this.handleUpdate}
              isEdit={isEdit}
            />
            <Button variant="danger" onClick={this.handleDelete}>
              Delete
            </Button>
          </Modal.Footer>
        </Modal>
      </>
    );
  }
}

export default PostView;
