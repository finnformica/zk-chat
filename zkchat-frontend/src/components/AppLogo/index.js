import Image from "next/image";
import styles from "./app-logo.module.css";

const AppLogo = ({ main = true }) => {
  return (
    <div className={main ? styles.center : styles.center2}>
      <Image
        className={styles.logo}
        src="/privacy-eye.png"
        alt="zkChat logo"
        width={64}
        height={64}
        priority
      />
      <h1 className={styles.title}>zkChat</h1>
    </div>
  );
};

export default AppLogo;
