import styles from "./header.module.css";

const Header = ({ left, right }) => {
  return (
    <div className={styles.description}>
      {left}
      <div>{right}</div>
    </div>
  );
};

export default Header;
