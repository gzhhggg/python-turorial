import { DefaultService } from "@/client";


async function main() {
    const response = await DefaultService.createClientClientsPost({
        requestBody: {
            name: "aaaaa",
        },
    });
    console.log(response.name);
}

