import React from "react";
import styles from "./component.module.css";

const MainContainer = ({ children }) => {
  return <main className={styles.main}>{children}</main>;
};

export default MainContainer;
