"use client";
import React, { useEffect } from "react";

import { signIn, signOut, useSession } from "next-auth/react";

import Header from "@/components/Header";
import MainContainer from "@/components/MainContainer";

import styles from "./page.module.css";

const VerifierPage = () => {
  const { data: session } = useSession();

  useEffect(() => {
    if (session) {
      console.log(session);
    }
  }, [session]);

  return (
    <MainContainer>
      <Header left={<p style={{ fontSize: "2rem" }}>zkChat : Verifier</p>} />
      <div>
        {!session ? (
          <button className={styles.button} onClick={() => signIn("keycloak")}>
            Login
          </button>
        ) : (
          <button className={styles.button} onClick={() => signOut("keycloak")}>
            Logout
          </button>
        )}
      </div>
      {!session ? (
        <p>Not signed in</p>
      ) : (
        <p>Signed in as user {session.user.name}</p>
      )}
    </MainContainer>
  );
};

export default VerifierPage;
