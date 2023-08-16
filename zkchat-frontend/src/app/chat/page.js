"use client";
import React, { useState, useEffect } from "react";
import { useSession, signIn } from "next-auth/react";

import Header from "@/components/Header";
import TextInput from "@/components/TextInput";
import ChatRow from "@/components/ChatRow";
import MainContainer from "@/components/MainContainer";

import styles from "./page.module.css";

const ChatPage = () => {
  const [chat, setChat] = useState({});

  const { data: session, status } = useSession();

  useEffect(() => {
    const initChat = {
      user: [],
      bot: [],
    };
    localStorage.setItem("chat", JSON.stringify(initChat));
    setChat(initChat);

    window.addEventListener("storage", (e) => {
      setChat(JSON.parse(localStorage.getItem("chat")));
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

      {chat && chat.user && chat.user.length > 0 && (
        <div className={styles.container}>
          {chat.user.map((message, index) => (
            <React.Fragment key={index}>
              <ChatRow message={message} />
              <ChatRow message={chat.bot[index]} />
            </React.Fragment>
          ))}
        </div>
      )}

      <TextInput />
    </MainContainer>
  );
};

export default ChatPage;
