#include "NpcRagHttp.h"
#include "HttpModule.h"
#include "Interfaces/IHttpResponse.h"
#include "Json.h"
#include "JsonUtilities.h"

// Sets default values
ANpcRagHttp::ANpcRagHttp()
{
    // Set this actor to call Tick() every frame. You can turn this off to improve performance if you don't need it.
    PrimaryActorTick.bCanEverTick = true;
}

// Called when the game starts or when spawned
void ANpcRagHttp::BeginPlay()
{
    Super::BeginPlay();
}

// Called every frame
void ANpcRagHttp::Tick(float DeltaTime)
{
    Super::Tick(DeltaTime);
}

void ANpcRagHttp::MakeHttpRequest(const FString& JsonBody)
{
    // Create the request
    TSharedRef<IHttpRequest, ESPMode::ThreadSafe> Request = FHttpModule::Get().CreateRequest();
    Request->OnProcessRequestComplete().BindUObject(this, &ANpcRagHttp::OnResponseReceived);
    Request->SetURL(TEXT("SERVER URL HERE - REMOVING FOR GITHUB")); // Replace with your API URL
    Request->SetVerb(TEXT("POST"));
    Request->SetHeader(TEXT("Content-Type"), TEXT("application/json"));
    Request->SetContentAsString(JsonBody);
    Request->ProcessRequest();
}

void ANpcRagHttp::OnResponseReceived(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful)
{
    if (bWasSuccessful && Response.IsValid())
    {
        FString ResponseString = Response->GetContentAsString();
        UE_LOG(LogTemp, Log, TEXT("HTTP Request successful. Full Response: %s"), *ResponseString);

        // Parse the JSON response
        TSharedPtr<FJsonObject> JsonObject;
        TSharedRef<TJsonReader<>> Reader = TJsonReaderFactory<>::Create(ResponseString);

        if (FJsonSerializer::Deserialize(Reader, JsonObject) && JsonObject.IsValid())
        {
            FString ParsedResponse;
            if (JsonObject->TryGetStringField("response", ParsedResponse))
            {
                ResponseContent = ParsedResponse;
                UE_LOG(LogTemp, Log, TEXT("Parsed Response: %s"), *ResponseContent);
            }
            else
            {
                UE_LOG(LogTemp, Error, TEXT("Failed to get 'response' field from JSON"));
                ResponseContent = TEXT("Failed to parse response");
            }
        }
        else
        {
            UE_LOG(LogTemp, Error, TEXT("Failed to parse JSON response"));
            ResponseContent = TEXT("Failed to parse JSON response");
        }
    }
    else
    {
        UE_LOG(LogTemp, Error, TEXT("HTTP Request failed."));
        ResponseContent = TEXT("HTTP Request failed.");
    }
    OnHttpResponseReceived.Broadcast(); // Broadcast the delegate
}

FString ANpcRagHttp::GetResponseContent() const
{
    return ResponseContent;
}
