import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'About the Documentation',
    iconPath: require('@site/static/img/docs.png').default,
    description: (
      <>
       This documentation provides detailed instructions for setting up, managing, and optimizing hospital data using the Shyntea system.
      </>
    ),
  },
  {
    title: 'What You will Find',
    iconPath: require('@site/static/img/magnifying-glass.png').default,
    description: (
      <>
        From foundational data management to advanced practices, this resource helps you master the use of Shyntea in hospital environments.
      </>
    ),
  },
  {
    title: 'Start Exploring',
    iconPath: require('@site/static/img/rocket.png').default,
    description: (
      <>
        Dive into the documentation to learn best practices and maximize efficiency in data management with Shyntea.
      </>
    ),
  },
];

function Feature({ iconPath, title, description }) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <img src={iconPath} alt="" className={styles.featureSvg} role="img" /> {/* Cambia Svg por img */}
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
