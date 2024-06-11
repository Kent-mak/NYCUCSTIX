import * as React from "react";
import NavBar from './NavBar';
import EventCard from './EventCard';

const Home: React.FC = () => {
  const events = [
    {
      imageSrc: "https://cdn.builder.io/api/v1/image/assets/TEMP/2138bbe1b266dd8ca7cbf06b82cf281c39bc54a15e9afd1706dfe83545401740?apiKey=81ea71315c0e494985346d51166aaad4&",
      imageAlt: "理想渾蛋",
      title: "理想渾蛋",
      subtitle: "理想渾蛋演唱會",
      date: "2024.05.17 (五)",
      buttonText: "我要買",
      buttonAriaLabel: "Buy ticket for 理想渾蛋演唱會"
    },
    {
      imageSrc: "https://cdn.builder.io/api/v1/image/assets/TEMP/4d0a72905941138186f9c49402f34e3de88f559eaf706da4dacf68093673bf26?apiKey=81ea71315c0e494985346d51166aaad4&",
      imageAlt: "芒果醬",
      title: "芒果醬",
      subtitle: "九彎十八拐",
      date: "2024.06.03 (六)",
      buttonText: "我要買",
      buttonAriaLabel: "Buy ticket for 九彎十八拐"
    },
    {
      imageSrc: "https://cdn.builder.io/api/v1/image/assets/TEMP/89c94dcb62483d83886178f37ee0c433e54f5bd19379c831127d8144d4fe5fc5?apiKey=81ea71315c0e494985346d51166aaad4&",
      imageAlt: "美秀集團",
      title: "美秀集團",
      subtitle: "美秀專場",
      date: "2024.08.15 (日)",
      buttonText: "我要買",
      buttonAriaLabel: "Buy ticket for 美秀專場"
    }
  ];

  return (
    <div className="flex flex-col">
      <NavBar />
      <div className="flex-grow flex justify-center items-center px-16 py-20 bg-white">
        <main className="flex flex-col items-center w-full">
          <header className="flex flex-col items-center w-full max-w-[1057px]">
            <h1 className="text-4xl font-semibold tracking-tighter leading-9 text-black">現正熱賣</h1>
            <p className="mt-2 text-base leading-6 text-ellipsis text-zinc-700">獨立樂團</p>
          </header>
          <section className="flex flex-wrap justify-center gap-8 w-full max-w-[1057px] mt-12">
            {events.map((event, index) => (
              <EventCard
                key={index}
                imageSrc={event.imageSrc}
                imageAlt={event.imageAlt}
                title={event.title}
                subtitle={event.subtitle}
                date={event.date}
                buttonText={event.buttonText}
                buttonAriaLabel={event.buttonAriaLabel}
              />
            ))}
          </section>
        </main>
      </div>
    </div>
  );
};

export default Home;