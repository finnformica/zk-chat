"use client";
import { useState } from "react";
import styles from "./component.module.css";

import { BiSend } from "react-icons/bi";
import { ImSpinner8 } from "react-icons/im";

const TextInput = ({ loading }) => {
  const [text, setText] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (loading) return;

    const chat = JSON.parse(localStorage.getItem("chat"));
    localStorage.setItem(
      "chat",
      JSON.stringify({
        ...chat,
        user: [...chat.user, text],
      })
    );
    dispatchEvent(new Event("storage"));

    setText("");
  };

  return (
    <form onSubmit={handleSubmit} className={styles.container}>
      <input
        type="text"
        className={styles.textInput}
        value={text}
        onChange={(e) => setText(e.target.value)}
      />
      <button
        disabled={loading}
        className={styles.button}
        onClick={handleSubmit}
      >
        {loading ? (
          <ImSpinner8 size="1.5rem" className={styles.spin} />
        ) : (
          <BiSend size="1.5rem" />
        )}
      </button>
    </form>
  );
};

export default TextInput;
