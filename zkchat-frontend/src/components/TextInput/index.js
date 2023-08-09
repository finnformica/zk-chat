import styles from "./component.module.css";

import { BiSend } from "react-icons/bi";

const TextInput = () => {
  return (
    <div className={styles.container}>
      <input type="text" className={styles.textInput} />
      <button className={styles.button}>
        <BiSend size="1.5rem" />
      </button>
    </div>
  );
};

export default TextInput;
