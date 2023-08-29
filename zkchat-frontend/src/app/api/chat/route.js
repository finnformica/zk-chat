import { NextResponse } from "next/server";
import { getServerSession } from "next-auth";
import { authOptions } from "../auth/[...nextauth]/route";

export async function POST(req, res) {
  const session = await getServerSession(authOptions);
  const json = await req.json();

  console.log(json);

  if (session) {
    const body = {
      message: json.message,
      history: {
        user_messages: [],
        bot_messages: [],
      },
      api_key: process.env.THIRD_PARTY_SERVICE_APIKEY,
    };
    const data = await fetch(process.env.THIRD_PARTY_SERVICE_URL, {
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
