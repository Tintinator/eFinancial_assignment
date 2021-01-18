import React from "react";
import "bootstrap/dist/css/bootstrap.min.css";
import "../styles/Home.css";

import NewEntry from "./NewEntry";

function Home() {
  return (
    <div className="Home">
      <div className="TitleContainer">
        <h1 className="Name">Tin's Blog</h1>
        <NewEntry />
      </div>
      <div className="ContentContainer"></div>
    </div>
  );
}

export default Home;
