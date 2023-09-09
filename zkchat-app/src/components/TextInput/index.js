"use client";
import { useState } from "react";
import styles from "./component.module.css";

import { BiSend } from "react-icons/bi";
import { ImSpinner8 } from "react-icons/im";

const TextInput = () => {
  const [text, setText] = useState("");
  const [loading, setLoading] = useState(false);

  const storeUserMessage = () => {
    const chat = JSON.parse(localStorage.getItem("chat"));
    localStorage.setItem(
      "chat",
      JSON.stringify({
        ...chat,
        user: [...chat.user, "USER: " + text],
      })
    );
    dispatchEvent(new Event("storage"));

    setText("");
  };

  const fetchBotMessage = async () => {
    const data = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/chat`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({
        message: text,
      }),
    })
      .then((res) => res.json())
      .catch((err) => console.log(err))
      .finally(() => setLoading(false));

    const chat = JSON.parse(localStorage.getItem("chat"));
    localStorage.setItem(
      "chat",
      JSON.stringify({
        ...chat,
        bot: [...chat.bot, "BOT: " + data?.message],
      })
    );
    dispatchEvent(new Event("storage"));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (loading) return;

    setLoading(true);

    storeUserMessage();
    fetchBotMessage();
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
