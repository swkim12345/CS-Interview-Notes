### 프로세스와 스레드의 차이점은 무엇인가요?

### 프로세스와 스레드의 구조와 장단점은 무엇인가요?

- 프로세스는 운영체제에서 실행되는 독립적인 실행 단위로, 프로그램이 메모리에 적재되면 프로세스로 동작합니다. 프로세스는 코드, 데이터, 힙, 스택 등 각자 독립된 메모리 공간을 할당받아 실행되며, 다른 프로세스와 메모리를 공유하지 않습니다. 반면, 스레드는 프로세스 내에서 실행되는 작업 단위로, 동일한 프로세스 내에서 코드, 데이터, 힙을 공유하지만, 스택은 개별적으로 할당됩니다. 이를 통해 스레드는 가벼운 실행 단위로 동작하며, 프로세스보다 빠른 데이터 공유가 가능하지만, 공유된 메모리로 인해 하나의 스레드에서 오류가 발생하면 다른 스레드에도 영향을 미칠 수 있습니다. 프로세스의 장점은 독립적인 메모리 공간을 가지므로 하나의 프로세스가 오류를 일으켜도 다른 프로세스에 영향을 주지 않는다는 점입니다. 그러나 프로세스 간 통신(IPC, Inter-Process Communication)이 필요할 경우 추가적인 비용과 복잡성이 발생하는 단점이 있습니다.

**추가하면 좋을 점**
프로세스와 스레드의 생성 비용: 프로세스는 독립적인 메모리 공간을 가지므로 생성 및 관리 비용이 높은 반면, 스레드는 비교적 적은 비용으로 생성됩니다.

멀티프로세싱과 멀티스레딩: 멀티프로세싱은 안정적이지만 자원 소모가 큰 반면, 멀티스레딩은 효율적이지만 동기화 이슈 등이 발생할 수 있다는 점을 언급하면 좋습니다.

### 시스템 콜이 무엇이며, 왜 중요한가요?

시스템 콜은 사용자 모드에서 커널 모드로 전환할 때 사용하는 인터페이스로, 프로세스가 운영체제의 자원에 접근할 수 있게 해주는 역할을 합니다. 또한, 커널 모드는 높은 권한을 요구하기 때문에 신중하게 다뤄져야 한다

### 운영체제에서 메모리 관리 기법으로 사용되는 페이징과 세그멘테이션의 차이점은 무엇인가요?

페이징은 프로세스를 일정한 크기의 고정된 단위로 나누어 저장하는 기법으로, 이 단위를 **페이지(Page)**라고 합니다. 실제 물리 메모리도 동일한 크기의 블록으로 나누어 관리하는데, 이를 **프레임(Frame)**이라고 합니다. 프로세스의 페이지는 메모리의 프레임과 매핑되어 저장되며, 이를 통해 프로세스의 코드, 데이터, 힙, 스택 등을 메모리에 적재할 수 있습니다.

그러나 페이징에서는 **내부 단편화(Internal Fragmentation)**가 발생할 수 있습니다. 예를 들어, 500MB 크기의 프로세스를 30MB 크기의 페이지로 나누면 마지막 페이지가 20MB만 사용되고 나머지 10MB는 낭비되는 문제가 발생합니다.

반면, **세그멘테이션(Segmentation)**은 프로세스를 코드, 데이터, 힙, 스택과 같은 논리적 단위에 따라 가변 크기의 블록(세그먼트)으로 나누는 방식입니다. 페이징과 달리 각 세그먼트는 크기가 다를 수 있으며, 이를 물리 메모리에 적재하는 과정에서 **외부 단편화(External Fragmentation)**가 발생할 수 있습니다.

두 기법의 공통점은 **불연속적 메모리 할당을 지원**하여 프로세스를 여러 위치에 나누어 저장할 수 있다는 점입니다.

### 운영체제에서 동기화 문제는 무엇이며, 이를 해결하기 위한 방법으로는 무엇이 있나요?

뮤텍스(Mutex): 한 번에 하나의 스레드만 공유 자원에 접근할 수 있도록 하는 락 메커니즘입니다.
세마포어(Semaphore): 뮤텍스와 비슷하지만, 한 번에 여러 스레드가 접근할 수 있도록 제어할 수 있습니다.
모니터(Monitor): 뮤텍스와 조건 변수를 함께 사용해 동기화를 관리하는 방법입니다.
