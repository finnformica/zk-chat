import Link from "next/link";
import styles from "./page.module.css";
import Header from "@/components/Header";

import { FaArrowLeft } from "react-icons/fa";
import TextInput from "@/components/TextInput";

const HomeLink = () => {
  return (
    <Link href="/" className={styles.link}>
      <FaArrowLeft size="1.2rem" className={styles.arrow} />{" "}
      <h2 className={styles.homeLink}>Home</h2>
    </Link>
  );
};

const Chat = () => {
  return (
    <main className={styles.main}>
      <Header
        left={<p style={{ fontSize: "2rem" }}>zkChat</p>}
        right={<HomeLink />}
      />

      <TextInput />
    </main>
  );
};

export default Chat;
