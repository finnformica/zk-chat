import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "../auth/[...nextauth]/route";

export async function POST(request) {
  const session = await getServerSession(authOptions);
  if (session) {
    const body = {
      message: "hello world",
      history: {
        user_messages: [],
        bot_messages: [],
      },
      api_key: process.env.THIRD_PARTY_SERVICE_APIKEY,
    };
    console.log(body);
    const data = await fetch("http://localhost:10001/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },

      body: JSON.stringify(body),
    })
      .then((res) => res.json())
      .catch((err) => console.log(err));

    return NextResponse.json(data);
  } else {
    return NextResponse.json({
      error: "Not authenticated",
    });
  }
}

export async function GET(request) {
  return NextResponse.json({
    message: "Hello from the other side",
  });
}
