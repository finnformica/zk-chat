import Image from "next/image";
import styles from "./dev-logo.module.css";

const DevLogo = () => {
  return (
    <a href="https://finnformica.com" target="_blank" rel="noopener noreferrer">
      <Image
        src="/dev-logo.png"
        alt="finnformica dev logo"
        width={30}
        height={30}
        priority
      />
      <span className={styles.name}>@finnformica</span>
    </a>
  );
};

export default DevLogo;
