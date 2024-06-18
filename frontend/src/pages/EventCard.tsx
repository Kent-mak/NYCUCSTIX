import * as React from "react";
import { useNavigate } from "react-router-dom";

type EventCardProps = {
  imageSrc: string;
  imageAlt: string;
  title: string;
  subtitle: string;
  date: string;
  buttonText: string;
  buttonAriaLabel: string;
};

const EventCard: React.FC<EventCardProps> = ({
  imageSrc,
  imageAlt,
  title,
  subtitle,
  date,
  buttonText,
  buttonAriaLabel
}) => {
  const navigate = useNavigate();

  const handleButtonClick = () => {
    navigate('/event');
  };

  return (
    <article className="flex flex-col w-[33%] max-md:ml-0 max-md:w-full">
      <section className="flex flex-col grow text-xl leading-8 text-black max-md:mt-10">
        <figure className="overflow-hidden relative flex-col justify-center items-start px-4 pt-4 pb-36 w-full text-3xl font-semibold tracking-tighter leading-8 text-white whitespace-nowrap rounded-lg aspect-square max-md:pr-5 max-md:pb-10">
          <img loading="lazy" src={imageSrc} alt={imageAlt} className="object-cover absolute inset-0 size-full" />
          <figcaption>{title}</figcaption>
        </figure>
        <h2 className="mt-3 font-medium text-ellipsis">{subtitle}</h2>
        <time className="text-base text-ellipsis text-zinc-700">{date}</time>
        <button
          onClick={handleButtonClick}
          aria-label={buttonAriaLabel}
          className="justify-center px-4 py-1.5 mt-3 font-bold whitespace-nowrap bg-yellow-500 rounded-lg max-md:px-5"
        >
          {buttonText}
        </button>
      </section>
    </article>
  );
};

export default EventCard;
