import Link from "next/link";
import styles from "./page.module.css";
import Header from "@/components/Header";
import DevLogo from "@/components/DevLogo";
import AppLogo from "@/components/AppLogo";

export default function Home() {
  return (
    <main className={styles.main}>
      <Header
        left={
          <p>
            Get started by visiting the&nbsp;
            <code className={styles.code}>Issuer</code>
          </p>
        }
        right={<DevLogo />}
      />
      <AppLogo />

      <div className={styles.grid}>
        <Link
          href="https://email-verification.vonx.io/"
          className={styles.card}
          target="_blank"
        >
          <h2>
            Issuer <span>-&gt;</span>
          </h2>
          <p>Request a zero-knowledge Verifiable Credential.</p>
        </Link>
        <Link href="/verifier" className={styles.card}>
          <h2>
            Verifier <span>-&gt;</span>
          </h2>
          <p>Log in using a valid Verifiable Credential.</p>
        </Link>
        <Link href="/learn" className={styles.card}>
          <h2>
            Learn <span>-&gt;</span>
          </h2>
          <p>Learn about zkChat and how it protects the privacy its users!</p>
        </Link>

        <Link href="/chat" className={styles.card}>
          <h2>
            Chat <span>-&gt;</span>
          </h2>
          <p>Interact with ChatGPT anonymously using zkChat.</p>
        </Link>
      </div>
    </main>
  );
}
