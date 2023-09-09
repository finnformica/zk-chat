import React from "react";

import Header from "@/components/Header";
import MainContainer from "@/components/MainContainer";

const IssuerPage = () => {
  return (
    <MainContainer>
      <Header left={<p style={{ fontSize: "2rem" }}>zkChat : Issuer</p>} />
    </MainContainer>
  );
};

export default IssuerPage;
