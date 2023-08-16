import React from "react";

import Header from "@/components/Header";
import MainContainer from "@/components/MainContainer";

const LearnPage = () => {
  return (
    <MainContainer>
      <Header left={<p style={{ fontSize: "2rem" }}>zkChat : Learn</p>} />
    </MainContainer>
  );
};

export default LearnPage;
