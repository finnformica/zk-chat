import Link from "next/link";
import { FaArrowLeft } from "react-icons/fa";

import styles from "./header.module.css";

const HomeLink = () => {
  return (
    <Link href="/" className={styles.link}>
      <FaArrowLeft size="1.2rem" className={styles.arrow} />{" "}
      <h2 className={styles.homeLink}>Home</h2>
    </Link>
  );
};

const Header = ({ left, right }) => {
  return (
    <div className={styles.description}>
      {left}
      {right && <div>{right}</div>}
      {!right && <HomeLink />}
    </div>
  );
};

export default Header;
