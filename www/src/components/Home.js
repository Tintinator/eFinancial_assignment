import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/Home.css";

import NewEntry from "./NewEntry";
import PostList from "./PostList";
import { getPosts } from "../api/BlogCommands";

class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      isFetching: false,
      entryData: [],
    };
  }

  componentDidMount() {
    this.fetchPostData();
    this.timer = setInterval(() => this.fetchPostData(), 60000);
  }

  componentWillUnmount() {
    clearInterval(this.timer);
    this.timer = null;
  }

  async fetchPostData() {
    try {
      this.setState({ ...this.state, isFetching: true });
      const response = await getPosts();
      this.setState({ entryData: response, isFetching: false });
    } catch (e) {
      this.setState({ ...this.state, isFetching: false });
    }
  }

  render() {
    const { entryData, isFetching } = this.state;

    return (
      <div className="Home">
        <div className="TitleContainer">
          <h1 className="Name">Tin's Blog</h1>
          <NewEntry />
        </div>
        <div className="ContentContainer">
          <PostList data={entryData} isFetching={isFetching}></PostList>
        </div>
      </div>
    );
  }
}

export default Home;
