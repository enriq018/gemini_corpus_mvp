#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "HttpModule.h"
#include "NpcRagHttp.generated.h"  // This should be the last include

DECLARE_DYNAMIC_MULTICAST_DELEGATE(FOnHttpResponseReceived);

UCLASS()
class SECONDTRY_API ANpcRagHttp : public AActor
{
    GENERATED_BODY()

public:
    // Sets default values for this actor's properties
    ANpcRagHttp();

    // Function to make the HTTP request
    UFUNCTION(BlueprintCallable, Category = "HTTP")
    void MakeHttpRequest(const FString& JsonBody);

    // Function to get the response content
    UFUNCTION(BlueprintCallable, Category = "HTTP")
    FString GetResponseContent() const;

    // Delegate to notify when the HTTP response is received
    UPROPERTY(BlueprintAssignable, Category = "HTTP")
    FOnHttpResponseReceived OnHttpResponseReceived;

protected:
    // Called when the game starts or when spawned
    virtual void BeginPlay() override;

public:
    // Called every frame
    virtual void Tick(float DeltaTime) override;

private:
    // Function to handle the HTTP response
    void OnResponseReceived(FHttpRequestPtr Request, FHttpResponsePtr Response, bool bWasSuccessful);

    // Member variable to store the response content
    FString ResponseContent;
};
