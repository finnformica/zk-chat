"use client";
import { useState, useEffect } from "react";
import { useSession, signIn } from "next-auth/react";

import Header from "@/components/Header";
import TextInput from "@/components/TextInput";
import ChatRow from "@/components/ChatRow";
import MainContainer from "@/components/MainContainer";

import styles from "./page.module.css";

const Chat = () => {
  const [chat, setChat] = useState({});
  const [loadingChat, setLoadingChat] = useState(false);

  const { data: session, status } = useSession();

  useEffect(() => {
    localStorage.setItem(
      "chat",
      JSON.stringify({
        user: [],
        bot: [],
      })
    );

    window.addEventListener("storage", (e) => {
      console.log(JSON.parse(localStorage.getItem("chat")));
      setLoadingChat(true);

      setTimeout(() => {
        setLoadingChat(false);
      }, 3000);
    });
  }, []);

  if (status === "unauthenticated") {
    signIn("keycloak", { callbackUrl: "/chat" });
  }

  if (status !== "authenticated") {
    return <p>Loading...</p>;
  }

  return (
    <MainContainer>
      <Header left={<p style={{ fontSize: "2rem" }}>zkChat : Chat</p>} />

      <div className={styles.container}>
        <ChatRow />
        <ChatRow />
        <ChatRow />
      </div>

      <TextInput loading={loadingChat} />
    </MainContainer>
  );
};

export default Chat;
