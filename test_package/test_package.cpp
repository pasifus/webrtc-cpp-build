#include <stdlib.h>
#include <iostream>

#include <rtc_base/ssl_adapter.h>
#include <rtc_base/thread.h>
#include <api/peer_connection_interface.h>

int main() {
    rtc::InitializeSSL();

    auto network_thread = rtc::Thread::CreateWithSocketServer();
    network_thread->Start();
    auto worker_thread = rtc::Thread::Create();
    worker_thread->Start();
    auto signaling_thread = rtc::Thread::Create();
    signaling_thread->Start();
    webrtc::PeerConnectionFactoryDependencies deps;

    deps.network_thread  = network_thread.get();
    deps.worker_thread = worker_thread.get();
    deps.signaling_thread = signaling_thread.get();
    auto peer_connection_factory = webrtc::CreateModularPeerConnectionFactory(std::move(deps));
    if (peer_connection_factory.get() == nullptr) {
      exit(EXIT_FAILURE);
    }

    rtc::CleanupSSL();
    std::cout << "TEST PACKAGE OK!" << std::endl;
    return EXIT_SUCCESS;
}