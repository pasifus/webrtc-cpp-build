# Conan WebRTC Package

Cross platform native webrtc build. It's not easy to build [webrtc from chromium project](https://chromium.googlesource.com/external/webrtc). I tried to create automatic build using [Github Actions(https://github.com/features/actions)] and package includes and library to [Conan package manager](https://github.com/conan-io/conan). It's include cross-platform and cross-compile build process. All build runs on Github VM-machines. 
## Available Builds
| Platform | Architecture | Build Type | Compiler      | LibCXX        |
|----------|--------------|------------|---------------|---------------|
| Windows  | x86_64       | Release    | Visual Studio |               |
| Windows  | x86_64       | Debug      | Visual Studio |               |
| MacOS    | x86_64       | Release    | clang         |               |
| MacOS    | x86_64       | Debug      | clang         |               |
| MacOS    | arm64        | Release    | clang         |               |
| MacOS    | arm64        | Debug      | clang         |               |
| iOS      | arm64        | Release    | clang         |               |
| iOS      | arm64        | Debug      | clang         |               |
| iOS      | x86_64       | Release    | clang         |               |
| iOS      | x86_64       | Debug      | clang         |               |
| Linux    | x86_64       | Release    | gnu           | libstdc++11   |
| Linux    | x86_64       | Debug      | gnu           | libstdc++11   |
|          |              |            |               |               |

