import React from "react";
import styles from "./component.module.css";

const ChatRow = ({ message }) => {
  return <p className={styles.row}>{message}</p>;
};

export default ChatRow;
